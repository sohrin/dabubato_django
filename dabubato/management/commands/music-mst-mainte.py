from django.core.management.base import BaseCommand
from requests_html import HTMLSession
from dabubato.models import MstMusic
from django.utils import timezone
import math

# ※実行方法
# pipenv shell
# python manage.py music-mst-mainte

class Command(BaseCommand):
    def handle(self, *args, **options):

        # 曲リストページの配列
        music_list_page_url_list = [
            "http://textage.cc/score/index.html?sA11B00",
            "http://textage.cc/score/index.html?sB11B00"
        ]
        for music_list_page_url in music_list_page_url_list:
            print(f"■music_list_page_url:{music_list_page_url}")
            music_list_page_session = HTMLSession()
            music_list_page_response = music_list_page_session.get(music_list_page_url)

            # shift_jisのページをスクレイピングする際のUnicodeEncodeError対策
            music_list_page_response.content.decode("shift_jis")

            print("before render music_list_page...")
            # 結構重いので大きめにタイムアウト時間を取る必要あり
            music_list_page_response.html.render(timeout=300)
            print("after  render music_list_page!!!")

            # 文字化け対策
            music_list_page_response.html.encoding = "utf-8"

            # find()で要素を探索
            music_tr_list = music_list_page_response.html \
                .find("table")[1] \
                .find("tr")
            first_tr_flg = True
            for music_tr in music_tr_list:
                if first_tr_flg:
                    first_tr_flg = False
                    continue
                td_second = music_tr.find("td")[1]
                td_second_class = td_second.attrs["class"][0]
                music_deleted_flag = False
                if td_second_class.startswith("x"):
                    music_deleted_flag = True
                    music_tr_diff_code = td_second_class[2:3]
                else:
                    music_tr_diff_code = td_second_class[1:2]
                
                # 曲リストページの難易度コードを曲マスタで保持する難易度コードに変換
                if music_tr_diff_code == "n":
                    music_tr_diff_code_mstcode = "N"
                elif music_tr_diff_code == "h":
                    music_tr_diff_code_mstcode = "H"
                elif music_tr_diff_code == "a":
                    music_tr_diff_code_mstcode = "A"
                elif music_tr_diff_code == "x":
                    music_tr_diff_code_mstcode = "L"
                else:
                    raise Exception(f"想定外のmusic_tr_diff_code:{music_tr_diff_code}")

                # 曲名
                music_name = music_tr.find("td")[3].text
                print(f"music_name:{music_name}")
                print(f"music_tr_diff_code_mstcode:{music_tr_diff_code_mstcode}")

                # 曲マスタを取得
                old_music_mst_list = MstMusic.objects.filter(
                    music_name = music_name,
                    difficulty_code = music_tr_diff_code_mstcode
                )
                if len(old_music_mst_list) == 0:
                    old_music_mst = None
                elif len(old_music_mst_list) == 1:
                    old_music_mst = old_music_mst_list[0]
                else:
                    raise Exception("複数レコード取得は想定外")

                if music_deleted_flag:
                    if old_music_mst is not None:
                        setattr(mst_music, "music_deleted_flag", \
                            music_deleted_flag)
                        setattr(mst_music, "upd_user", \
                            "music-mst-mainte.py")
                        setattr(mst_music, "upd_date", \
                            timezone.localtime())
                        old_music_mst.save()

                    continue

                else:
                    # レコードがすでに存在する場合は何もしない
                    if old_music_mst is not None:
                        print("MstMusic exists.")
                        continue

                    # 譜面ページURL
                    try:
                        note_page_url = "http://textage.cc/score/" \
                                    + td_second.find("a")[0] \
                                            .attrs["href"]
                    except Exception:
                        # aタグがない＝譜面ページがまだない
                        continue

                    # 譜面ページにアクセス
                    music_page_session = HTMLSession()
                    music_page_response = music_page_session.get(note_page_url)
                    music_page_response.content.decode("shift_jis")
                    print("before render music_page...")
                    music_page_response.html.render(timeout=300)
                    print("after  render music_page!!!")
                    music_page_response.html.encoding = "utf-8"

                    # 曲情報をパース(画面上部)
                    music_info_top_lines = music_page_response.html.find("nobr")[0]
                    music_info_top_line_text_arr = music_info_top_lines \
                                                       .text \
                                                       .split("\n")
                    for music_info_top_line_text in music_info_top_line_text_arr:
                        print(music_info_top_line_text)
                    music_info_style_diff = music_info_top_line_text_arr[1] \
                                                .replace("[", "") \
                                                .replace("]", "")
                    music_info_top_style_diff_arr = music_info_style_diff.split(" ")
                    music_info_top_others = music_info_top_line_text_arr[2] \
                                                .replace(" bpm:", ":::::") \
                                                .replace(" - ★", ":::::") \
                                                .replace(" Notes:", ":::::") \
                                                .split(":::::")
                    music_info_top_name_artist_arr = music_info_top_others[0].split(" / ")
                    music_info_top_bpm_arr = music_info_top_others[1].split("～")

                    # 曲情報をパース(画面下部)
                    music_info_bottom_line = music_page_response.html.find("table + font")[0]
                    print(music_info_bottom_line.text)
                    music_info_bottom_line_text_arr = music_info_bottom_line \
                                                          .text \
                                                          .replace(", ", ",") \
                                                          .split(" ", maxsplit=1) # TODO: DPのページは左右ノーツ数があるのでこのままだとだめ
                    music_info_bottom_score_border_arr = music_info_bottom_line_text_arr[0] \
                                                             .split(",")
                    music_info_bottom_special_notes_arr = music_info_bottom_line_text_arr[1] \
                                                             .replace("(", "") \
                                                             .replace(")", "") \
                                                             .split(" ")

                    # 曲名は設定済(music_name)

                    # 曲削除済フラグは設定済(music_deleted_flag)

                    # アーティスト名
                    artist_name = music_info_top_name_artist_arr[1]
                    
                    # ジャンル
                    genre = music_info_top_line_text_arr[0].replace("\"", "")

                    # 難易度(NORMAL or HYPER or ANOTHER or LEGGENDARIA)
                    difficulty_and_difficulty_code_map = {
                        "NORMAL"     : "N",
                        "HYPER"      : "H",
                        "ANOTHER"    : "A",
                        "LEGGENDARIA": "L",
                    }
                    difficulty_code = difficulty_and_difficulty_code_map.get(music_info_top_style_diff_arr[1])

                    # BPM
                    bpm_min = int(music_info_top_bpm_arr[0])
                    bpm_max = int(music_info_top_bpm_arr[0]) if len(music_info_top_bpm_arr) == 1 \
                         else int(music_info_top_bpm_arr[1])

                    # ★
                    level = int(music_info_top_others[2])

                    # SP総ノーツ数
                    sp_notes_num_all = int(music_info_top_others[3])

                    # SP特殊ノーツ数(スクラッチ)
                    sp_notes_num_scr = 0
                    # SP特殊ノーツ数(チャージノート)
                    sp_notes_num_cn  = 0
                    # SP特殊ノーツ数(バックスピンスクラッチ)
                    sp_notes_num_bss = 0
                    for special_notes_info in music_info_bottom_special_notes_arr:
                        special_notes_info_arr = special_notes_info.split("=")
                        if special_notes_info_arr[0] == "SCR":
                            sp_notes_num_scr = int(special_notes_info_arr[1])
                        elif special_notes_info_arr[0] == "CN":
                            sp_notes_num_cn  = int(special_notes_info_arr[1])
                        elif special_notes_info_arr[0] == "BSS":
                            sp_notes_num_bss = int(special_notes_info_arr[1])
                        else:
                            raise Exception(f"想定外の特殊ノーツ]{special_notes_info_arr[0]}")

                    # スコアボーダー
                    sp_score_border_aaa = int(music_info_bottom_score_border_arr[0].replace("AAA:", ""))
                    sp_score_border_aa  = int(music_info_bottom_score_border_arr[1].replace("AA:", ""))
                    sp_score_border_a   = int(music_info_bottom_score_border_arr[2].replace("A:", ""))

                    # DB用カラムの計算・設定
                    # TODO: CN、BSSは開始・終了で2ノーツ扱い
                    db_notes_num_scr = 0
                    db_notes_num_cn = sp_notes_num_cn * 2
                    db_notes_num_bss = 0
                    db_notes_num_all = sp_notes_num_all * 2 \
                                     - sp_notes_num_scr \
                                     - sp_notes_num_bss * 2
                    db_score_max = db_notes_num_all * 2
                    db_score_border_maxminus = math.ceil(db_notes_num_all * 2 * 8.5 / 9)
                    db_score_border_aaa = math.ceil(db_notes_num_all * 2 * 8 / 9)
                    db_score_border_aa = math.ceil(db_notes_num_all * 2 * 7 / 9)
                    db_score_border_a = math.ceil(db_notes_num_all * 2 * 6 / 9)

                    # TODO: 更新対応
                    mst_music = MstMusic()
                    setattr(mst_music, "music_name", \
                        music_name)
                    setattr(mst_music, "music_deleted_flag", \
                        music_deleted_flag)
                    setattr(mst_music, "artist_name", \
                        artist_name)
                    setattr(mst_music, "genre", \
                        genre)
                    setattr(mst_music, "difficulty_code", \
                        difficulty_code)
                    setattr(mst_music, "bpm_min", \
                        bpm_min)
                    setattr(mst_music, "bpm_max", \
                        bpm_max)
                    setattr(mst_music, "level", \
                        level)
                    setattr(mst_music, "sp_notes_num_all", \
                        sp_notes_num_all)
                    setattr(mst_music, "sp_notes_num_scr", \
                        sp_notes_num_scr)
                    setattr(mst_music, "sp_notes_num_cn", \
                        sp_notes_num_cn)
                    setattr(mst_music, "sp_notes_num_bss", \
                        sp_notes_num_bss)
                    setattr(mst_music, "sp_score_max", \
                        9999) # TODO: calc and set
                    setattr(mst_music, "sp_score_border_maxminus", \
                        9999) # TODO: calc and set
                    setattr(mst_music, "sp_score_border_aaa", \
                        sp_score_border_aaa)
                    setattr(mst_music, "sp_score_border_aa", \
                        sp_score_border_aa)
                    setattr(mst_music, "sp_score_border_a", \
                        sp_score_border_a)
                    setattr(mst_music, "dp_notes_num_all", \
                        9999) # TODO: calc and set
                    setattr(mst_music, "dp_notes_num_scr", \
                        9999) # TODO: calc and set
                    setattr(mst_music, "dp_notes_num_cn", \
                        9999) # TODO: calc and set
                    setattr(mst_music, "dp_notes_num_bss", \
                        9999) # TODO: calc and set
                    setattr(mst_music, "dp_score_max", \
                        9999) # TODO: calc and set
                    setattr(mst_music, "dp_score_border_maxminus", \
                        9999) # TODO: calc and set
                    setattr(mst_music, "dp_score_border_aaa", \
                        9999) # TODO: calc and set
                    setattr(mst_music, "dp_score_border_aa", \
                        9999) # TODO: calc and set
                    setattr(mst_music, "dp_score_border_a", \
                        9999) # TODO: calc and set
                    setattr(mst_music, "db_notes_num_all", \
                        db_notes_num_all)
                    setattr(mst_music, "db_notes_num_scr", \
                        db_notes_num_scr)
                    setattr(mst_music, "db_notes_num_cn", \
                        db_notes_num_cn)
                    setattr(mst_music, "db_notes_num_bss", \
                        db_notes_num_bss)
                    setattr(mst_music, "db_score_max", \
                        db_score_max)
                    setattr(mst_music, "db_score_border_maxminus", \
                        db_score_border_maxminus)
                    setattr(mst_music, "db_score_border_aaa", \
                        db_score_border_aaa)
                    setattr(mst_music, "db_score_border_aa", \
                        db_score_border_aa)
                    setattr(mst_music, "db_score_border_a", \
                        db_score_border_a)
                    setattr(mst_music, "db_withscr_notes_num_all", \
                        9999) # TODO: calc and set
                    setattr(mst_music, "db_withscr_notes_num_scr", \
                        9999) # TODO: calc and set
                    setattr(mst_music, "db_withscr_notes_num_cn", \
                        9999) # TODO: calc and set
                    setattr(mst_music, "db_withscr_notes_num_bss", \
                        9999) # TODO: calc and set
                    setattr(mst_music, "db_withscr_score_max", \
                        9999) # TODO: calc and set
                    setattr(mst_music, "db_withscr_score_border_maxminus", \
                        9999) # TODO: calc and set
                    setattr(mst_music, "db_withscr_score_border_aaa", \
                        9999) # TODO: calc and set
                    setattr(mst_music, "db_withscr_score_border_aa", \
                        9999) # TODO: calc and set
                    setattr(mst_music, "db_withscr_score_border_a", \
                        9999) # TODO: calc and set
                    setattr(mst_music, "note_page_url", \
                        note_page_url)
                    setattr(mst_music, "ins_user", \
                        "music-mst-mainte.py")
                    setattr(mst_music, "ins_date", \
                        timezone.localtime())
                    setattr(mst_music, "upd_user", \
                        "music-mst-mainte.py")
                    setattr(mst_music, "upd_date", \
                        timezone.localtime())
                    mst_music.save()
                    
                    # # TODO: breakしない
                    # break
