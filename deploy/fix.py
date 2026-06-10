import re

with open(r'C:\Users\admin\Desktop\stitch_\deploy\html.final.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Map: Google URL key → local filename
url_map = {
    'AB6AXuAo0R2FRDpjhRWEW8080PG6re-cKawgkpqUTXdWsa0Dsccw2G2zNjsJALvYXt-KJahx9nGmPnU_4qeoItfAdxZ0w9LdXdGTsxnPZvugD7-_gz5plPallD8FggCdAYemtYpxrCJoJf3TQMBGkSHChNKhbjZ70_eJZ8RRelCqBHhpspOfUfy5ERw767uC957UHrtHaQTR5bFaPZya_aGbTTzidrsAd1R8ED3zs1bshtsNtMC08WSrPH4rJwQBQXGaZHVv0yLiJ3yaz8g': 'img/向日葵.png',  # joy
    'AB6AXuDXvyLNIBEGzyMIsUvVEGYyUhkTGjIn_pL8G5_p20raCeum6m3_m8wNQ0knLgJxOVm0loSAxupH1AiRt9Gj9YxeuEdD3v6b4nSRpmqk231vKwhHH5ux6sMtrzulJoy65RbRoStAUZew7bIPIz1pmBCgZ7zgvuafNE3WWgpmqLMe9ol1iuLW5NylCT_YjZFzcwnG9vmNLqK_fWq3Iw0Fk_rC5x0R4BY6CbNA4N5Il4AB8Mldrvi-Oxl25hDeobUV6_lMvsw5sGY5Gcs': 'img/三叶草.png',  # calm
    'AB6AXuC9FsgIL0o0Cu-QZ7vgntIncObaxKENhwrKBEgI2Tb_lzRNIBMpCCjMhp-ag-6jCGo9xJ9pTZ2N9X1dNdaAIx4G_I5snsbcnk8DVu0I4aqd4cHddrCwH8nuLlgKWTeeoPzVl-m1DrTPFwnjYssKF2ZnL5y81B2fQwxfgTfNWNQGSC094JF4_ykq0wllqGlW_nqlcmo4m4V62bD6nzWO5pxkj4eYxFiDJHMs99pd2QughEYVTgluPTYf1mME_3tyB8OhdbZAUE_Y230': 'img/勿忘我.png',  # inspire
    'AB6AXuArsKztJseuASF0X-9lgpsVFizsFo85wPle8ckVkxIJbUePRu_JzT9gPTGDs7ztazO-X9tcJFh-SMvOWraT4ewauRHVSu_QJfn1ykNvzNNqrtliWlxR8Dbn5pCM0EZrX26I1F1_NjzMBR787ZTgjQapNpCMp-nNwMda9xw0FqK_ohfrfz0vCtXW01jEcJc0VYLeMtHXed5rpMHI-WsabtdMFWS7vhFcDZmtg8g5_-jRBo-nLT4xVBoZBARn5qioG4FFUBMLQ9Ux8zw': 'img/康乃馨.png',  # touch
    'AB6AXuBvizthZd1nqxaresUrS2iMZW8fynmiL61h_-H9yVSYV72xXvLr_iPSjlKXoxQuPcpF5I86hXcg1a3fblXJEpW5L2OIUtHtpC8yN3nv1cxLA1Ce-3C-u25-TuPOgQ-LDRVGKPlJTiWeKVnP1LHSPPLviBt-_ydgfTndwNp2dA1bn6wg_5utTilMSe1G3WEzF9x6CM7OF_V7pEo38zuPlWvl1FYQCKvgahUU8tuoKyRRbJ8jWT7XKd3ic3jP6UZMK--qRCt5DkzBPUI': 'img/星光花.png',  # sad
    'AB6AXuAx6_cvPSxdH2UuJJ-rkbfdgDgS4bvV1aZOaxj0Pfxhjgz20SQw6KplYBBmmQzVfzI48_H04HkFPAUQ8gQpWkSax-wJV6xyQ_LOCWMWXWb_QGqiZkqKs7dkUyQD5cx1cJH7_pb9Sk3ilrrb941NnJ7N_kfLdiVNIrLnnUY3SClL2ZM7mVVCVZqOcutl3ua-hmQVyM_nqWp7TfrQkF1yW5c-Wps6aHAU0xhTh8hAEBOMRhLb6yLz-0pX9_HrOcG2YP9gIlxnD6xyjvg': 'img/火焰花.png',  # angry
}

for key, path in url_map.items():
    c = c.replace(key, path)

# Replace fonts.googleapis.com -> fonts.googleapis.cn
c = c.replace('fonts.googleapis.com/css2?family=Material+Symbols+Outlined',
              'fonts.googleapis.cn/css2?family=Material+Symbols+Outlined')
c = c.replace('fonts.googleapis.com/css2?family=Noto+Serif',
              'fonts.googleapis.cn/css2?family=Noto+Serif')

# Remove background-image URLs (will break on github.io)
c = c.replace(
    "background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuCdLTawdAFacGQVz8kYAL8hh5r7zHrmnhEJhPP7v8ql58eYve60bOc_R8F92WTefl_i2-CcB8eDanjZu-H3vXr8o3hXkqhyoPurih02z0d5aNh5_X7MkvAUZDP2ruxMtK9igHbsKdwAvOzmTNcRwdYhmgGIT0-FWw1MF_gWdfe1lIALdt9MzmJWGIJXgSup0SyGQVAV4qe1J88_LNQYaLdfMsRYAGqzMMZ1tIurIOBMHnrNAO7ae7Oipa96FvwWVB3zizidrbTE_SU')",
    "background-image: none")
c = c.replace(
    "background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuCS1vnjN1TRsXqtAO0ptCZffP6i9Y1TyRDMeIUM5cSvK1F1eUewceX6G0l0hisIZxnUTh5wYyp92wERny4Vf_1hgLRVlrmuuMUoV81JQ91e_6pxRey0khcq8qIBIIQhKKRC-s_wPco0_GqCSXhVx7Fc2qemTSkQwJyeG-JydunIWoHeAHFEBFywj1nNBUe3D32ur30yj2p-uci87ix3GimJqKEC3HiA5bbyd6Y3uffOtfl_EWcp4AIt66E0322z7_UaBEMCHdk45pg')",
    "background-image: none")
c = c.replace(
    "background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuA5rp-KpnOE_CTX8MHPwrJo_TnOeLXGLVQi7Xqu8gQOD7hq_g7EEISBl-rwX8E5HU1x36soulbapx99E9iut3P_yjcA5U0utv9SpKSZKyA0YkoKjds6llUvTPtsqNBTlth2z91J9nMaA-XAc4n7nMbNqRvqXjNWmUVtDueXzIwS2BnzUf-dPqYOsyHQUzmh8QusSmWUtTGnh7ncH2CSMEL7DDtRa5CSBW6upQNpQ2FRpbNSfC7fqxwrQXFIho2YgZSVFuglvvaScbw')",
    "background-image: none")

with open(r'C:\Users\admin\Desktop\stitch_\deploy\html.final.html', 'w', encoding='utf-8') as f:
    f.write(c)

# Verify
has_google = 'lh3.googleusercontent.com' in c
has_local = 'img/向日葵' in c and 'img/三叶草' in c and 'img/火焰花' in c
print(f'Google URLs remaining: {has_google}')
print(f'Local paths present: {has_local}')
print('Done!')