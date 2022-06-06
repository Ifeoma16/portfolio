import webbrowser
import random

print(""" How is your mood?
1. Energetic
2. Anxious
3. Depressed
4. Calm/Relaxed
5. Content
6. Love
7. Random
""")

choice = int(input("Enter your choice: "))

if choice == 1:
    print(""" What genre do you desire?
1. Pop
2. Rock
3. Rap
4. Country
5. Jazz
    """)

    choice2 = int(input("Enter your choice: "))

    if choice2 == 1:
        energetic_pop = ['https://www.youtube.com/watch?v=uRoDyfQM-Cw', 'https://www.youtube.com/watch?v=lCAUfUCwyDA', 'https://www.youtube.com/watch?v=OPf0YbXqDm0&list=PL0m-fk7Zv9u3ikrG9H1UBD_wZNWyoy-tW&index=1']
        webbrowser.open(random.choice(energetic_pop))
    elif choice2 == 2:
        energetic_rock = ['https://www.youtube.com/watch?v=P62zPTims-g', 'https://www.youtube.com/watch?v=hTWKbfoikeg&list=PLJtpjlkBVF4z2o6DTE2mGa58ktnDUUE-F', 'https://www.youtube.com/watch?v=AtR3I4vYpqo&list=PLKHWKUwPVFz29C8OwSL7oZYu1EqQqav_K']
        webbrowser.open(random.choice(energetic_rock))
    elif choice2 == 3:
        energetic_rap = ['https://www.youtube.com/watch?v=RJPNjYVnJnk', 'https://www.youtube.com/watch?v=NQbkGDoD7B0&list=PLeed1JOctJVXF56Kvbg-Nueht4hTzCvfZ', 'https://www.youtube.com/watch?v=yQBImEeXNZ4&list=PLpD3_qiU0N7EQ4ghNV9J45IqENyzIuJ-D']
        webbrowser.open(random.choice(energetic_rap))
    elif choice2 == 4:
        energetic_country = ['https://www.youtube.com/watch?v=Tli__NYdSqI', 'https://www.youtube.com/watch?v=8zO6Wnmp1DU&list=PLx9ewCPgV2w3wNR6KcTDoxrMXKafY7nXJ', 'https://www.youtube.com/watch?v=KlXnApZ8Kq4&list=PL-QvSRz8uhNHt_5IcoQRlkb75crK-NOQ2']
        webbrowser.open(random.choice(energetic_country))
    elif choice2 == 5:
        energetic_jazz = ['https://www.youtube.com/watch?v=bdWUj2NYDYQ', 'https://www.youtube.com/watch?v=Q6cSTBfIGHk', 'https://www.youtube.com/watch?v=OFXC6PDyIBs']
        webbrowser.open(random.choice(energetic_jazz))

if choice == 2:
    print(""" What genre do you desire?
1. Pop
2. Rock
3. Country
4. Jazz
    """)

    choice3 = int(input("Enter your choice: "))

    if choice3 == 1:
        anxious_pop = ['https://www.youtube.com/watch?v=rA42kDhlMYI', 'https://www.youtube.com/watch?v=ca1kZ4RgZw4', 'https://www.youtube.com/watch?v=-b6ilyqXmTU']
        webbrowser.open(random.choice(anxious_pop))
    elif choice3 == 2:
        anxious_rock = ['https://www.youtube.com/watch?v=dCoONMpupl4', 'https://www.youtube.com/watch?v=MvHVzOREGUQ', 'https://www.youtube.com/watch?v=W9tkUovsZJ4']
        webbrowser.open(random.choice(anxious_rock))
    elif choice3 == 3:
        anxious_country = ['https://www.youtube.com/watch?v=sZFdLBrpjGY', 'https://www.youtube.com/watch?v=V3kcs2RNec8']
        webbrowser.open(random.choice(anxious_country))
    elif choice3 == 4:
        anxious_jazz = ['https://www.youtube.com/watch?v=neV3EPgvZ3g', 'https://www.youtube.com/watch?v=mSjMsdde-xQ', 'https://www.youtube.com/watch?v=5vV412eHGHc']
        webbrowser.open(random.choice(anxious_jazz))

if choice == 3:
    print(""" What genre do you desire?
1. Pop
2. Rock
3. Rap
4. Country
5. Jazz
    """)

    choice4 = int(input("Enter your choice: "))

    if choice4 == 1:
        depressed_pop = ['https://www.youtube.com/watch?v=Tl2JICdKvv0', 'https://www.youtube.com/watch?v=NMCgN4QK1Gw', 'https://www.youtube.com/watch?v=Jng4mtb2wIM']
        webbrowser.open(random.choice(depressed_pop))
    elif choice4 == 2:
        depressed_rock = ['https://www.youtube.com/watch?v=g8z-qP34-1Y&list=PLlOll-NAMPotWYOYkLqP4u16fERVfF56E', 'https://www.youtube.com/watch?v=8295rOMvtQI&list=PL2tb4KBOS-tlw4Drtem0GCyKkUqfvwzp7', 'https://www.youtube.com/watch?v=DnGdoEa1tPg&list=PL4Li1xClWQsEAg3LcXAJE3VJzzA8seXhD']
        webbrowser.open(random.choice(depressed_rock))
    elif choice4 == 3:
        depressed_rap = ['https://www.youtube.com/watch?v=5IhwJvvJ2VA&list=PLOARQUBDjA37xE6RX7G5naNjc1sT3p1_Y', 'https://www.youtube.com/watch?v=yQFBKx6eq8s&list=PLAknm6MHSp_Qz7gPCC31LI96HeC8fyYeV', 'https://www.youtube.com/watch?v=uAPUkgeiFVY&list=PL4xqRMQ2GXanzbtvdm2NNpXACQ8MSlVNA']
        webbrowser.open(random.choice(depressed_rap))
    elif choice4 == 4:
        depressed_country = ['https://www.youtube.com/watch?v=pF9buIk57P0', 'https://www.youtube.com/watch?v=YK3zs7EV6Tk&list=PLyl0dE5JtcL8QZQfv0Ji0P5qTqqIwR4lu', 'https://www.youtube.com/watch?v=eM213aMKTHg&list=PLvFYFNbi-IBHkSxfeh_Q-QKGsCRgYd72A']
        webbrowser.open(random.choice(depressed_country))
    elif choice4 == 5:
        depressed_jazz = ['https://www.youtube.com/watch?v=SbNfLNCaKqA', 'https://www.youtube.com/watch?v=ulGwHzrKOAU&list=PL3n7zMgQqsHhW_eVY2BZPKx6kyG10FWO1', 'https://www.youtube.com/watch?v=aaYkXg5eCG0']
        webbrowser.open(random.choice(depressed_jazz))

if choice == 4:
    print(""" What genre do you desire?
1. Pop
2. Rock
3. Rap
4. Country
5. Jazz
    """)

    choice5 = int(input("Enter yor choice: "))

    if choice5 == 1:
        calm_pop = ['https://www.youtube.com/watch?v=VqeGs0K7V2s', 'https://www.youtube.com/watch?v=2Vv-BfVoq4g&list=PL7v1FHGMOadDghZ1m-jEIUnVUsGMT9jbH', 'https://www.youtube.com/watch?v=GsPq9mzFNGY&list=PLic9OgMt4temXortBB2t2pGQN5fkJfrLN']
        webbrowser.open(random.choice(calm_pop))
    elif choice5 == 2:
        calm_rock = ['https://www.youtube.com/watch?v=xwtdhWltSIg&list=PLinS5uF49IBqNvkIBlLUg8rYPLOb21Z0U', 'https://www.youtube.com/watch?v=bx1Bh8ZvH84&list=PL_5OjOMdSPuxCs6uMRqQ4XemOSyMAupqq', 'https://www.youtube.com/watch?v=QmKxMyKJ2iM']
        webbrowser.open(random.choice(calm_rock))
    elif choice5 == 3:
        calm_rap = ['https://www.youtube.com/watch?v=zIrhcTkHX_A&list=PLkfIleCGpZLvw-pYVY9auGcK1A9QVG0Wp', 'https://www.youtube.com/watch?v=SsKT0s5J8ko&list=PL5F_lIxu0wUog5Ea5JvGm2LANEdduU9Rq', 'https://www.youtube.com/watch?v=WABOrIYhR94&list=PLgzTt0k8mXzEaqjkc-CeNg1q5YphbnY2E']
        webbrowser.open(random.choice(calm_rap))
    elif choice5 == 4:
        calm_country = ['https://www.youtube.com/watch?v=0xXD9-1mLBY&list=PLL4ZEHd9T5ZYheoYbj6Lr4Sc33HbztjQ7', 'https://www.youtube.com/watch?v=h7l5DF02Q9M', 'https://www.youtube.com/watch?v=3LR9sIVK6TI']
        webbrowser.open(random.choice(calm_country))
    elif choice5 == 5:
        calm_jazz = ['https://www.youtube.com/watch?v=_ApokDZMDDY', 'https://www.youtube.com/watch?v=EIw8SO6dadQ', 'https://www.youtube.com/watch?v=WgmCloGBBwY']
        webbrowser.open(random.choice(calm_jazz))

if choice == 5:
    print(""" What genre do you desire?
1. Pop
2. Rock
3. Rap
4. Jazz
    """)

    choice6 = int(input("Enter your choice: "))

    if choice6 == 1:
        content_pop = ['https://www.youtube.com/watch?v=xiUhNx24iZs', 'https://www.youtube.com/watch?v=bm0XIfbfKp4', 'https://www.youtube.com/watch?v=pJk1J5jcMZ4']
        webbrowser.open(random.choice(content_pop))
    elif choice6 == 2:
        content_rock = ['https://www.youtube.com/watch?v=Y_7cXDCNKEk', 'https://www.youtube.com/watch?v=4HANIw8ohII', 'https://www.youtube.com/watch?v=9NMtaypXZq8']
        webbrowser.open(random.choice(content_rock))
    elif choice6 == 3:
        content_rap = ['https://www.youtube.com/watch?v=sV2t3tW_JTQ&list=PLx4sLqBJV5wluHJria9hs1oYbv-mH6KV9', 'https://www.youtube.com/watch?v=30FyGBKWWDY']
        webbrowser.open(random.choice(content_rap))
    elif choice6 == 4:
        content_jazz = ['https://www.youtube.com/watch?v=F2EmooQ1Iag', 'https://www.youtube.com/watch?v=x4ygVwbOyJU', 'https://www.youtube.com/watch?v=gWaat4zZUn8']
        webbrowser.open(random.choice(content_jazz))

if choice == 6:
    print(""" What genre do you desire?
1. Pop
2. Rock
3. Rap
4. Country
5. Jazz
    """)

    choice7 = int(input("Enter your choice: "))

    if choice7 == 1:
        love_pop = ['https://www.youtube.com/watch?v=0Hdlh5A6DdY', 'https://www.youtube.com/watch?v=zeqW3apz7rs', 'https://www.youtube.com/watch?v=O2CIAKVTOrc&list=PL64G6j8ePNurWUzrnMGqpIQJ236oAkICT']
        webbrowser.open(random.choice(love_pop))
    elif choice7 == 2:
        love_rock = ['https://www.youtube.com/watch?v=UrIiLvg58SY&list=PLpOehZ0r85ixl-tdCfLqH7JmZe7BwxM2L', 'https://www.youtube.com/watch?v=e1nxy4lmjY4', 'https://www.youtube.com/watch?v=RiSfTyrvJlg&list=PLSTRVL236dhdkXTBPvWe3g3YxOjForMoz']
        webbrowser.open(random.choice(love_rock))
    elif choice7 == 3:
        love_rap = ['https://www.youtube.com/watch?v=rP09GUQFDFk&list=PL64G6j8ePNuqvxRcng0MhfgpY8eTk6-Hb', 'https://www.youtube.com/watch?v=jb6HZa151s8&list=PLenIjFQBKQH4PIiefeQUw_60IWEY1iPrp', 'https://www.youtube.com/watch?v=o_4TRygdoVY&list=PLZBFiRMzR7fLKtPObHWJVAD_-bcG3zh5q']
        webbrowser.open(random.choice(love_rap))
    elif choice7 == 4:
        love_country = ['https://www.youtube.com/watch?v=zDo0H8Fm7d0&list=PLSgTywHngOwMlZpv8laCA_wTQCC31yDg4', 'https://www.youtube.com/watch?v=Ti_SbTfNI7E', 'https://www.youtube.com/watch?v=rItv9i6c7AY&list=PLLDVfSPfze0vYOLuGg22o3F0ohSmcnOhl']
        webbrowser.open(random.choice(love_country))
    elif choice7 == 5:
        love_jazz = ['https://www.youtube.com/watch?v=_WcWHZc8s2I&list=PLh7IzJ3mFYA4KMbZHo93g9_ynU7XWAvQW', 'https://www.youtube.com/watch?v=R-xzfwDAn1I&list=PL7UF9wLCLmQEf3eVfW2ThDgNWKbmVe5qY', 'https://www.youtube.com/watch?v=3XsLBngWPqE']
        webbrowser.open(random.choice(love_jazz))

if choice == 7:
    random_playlist = ['https://www.youtube.com/watch?v=uRoDyfQM-Cw', 'https://www.youtube.com/watch?v=lCAUfUCwyDA', 'https://www.youtube.com/watch?v=OPf0YbXqDm0&list=PL0m-fk7Zv9u3ikrG9H1UBD_wZNWyoy-tW&index=1', 'https://www.youtube.com/watch?v=P62zPTims-g', 'https://www.youtube.com/watch?v=hTWKbfoikeg&list=PLJtpjlkBVF4z2o6DTE2mGa58ktnDUUE-F', 'https://www.youtube.com/watch?v=AtR3I4vYpqo&list=PLKHWKUwPVFz29C8OwSL7oZYu1EqQqav_K', 'https://www.youtube.com/watch?v=RJPNjYVnJnk', 'https://www.youtube.com/watch?v=NQbkGDoD7B0&list=PLeed1JOctJVXF56Kvbg-Nueht4hTzCvfZ', 'https://www.youtube.com/watch?v=yQBImEeXNZ4&list=PLpD3_qiU0N7EQ4ghNV9J45IqENyzIuJ-D', 'https://www.youtube.com/watch?v=Tli__NYdSqI', 'https://www.youtube.com/watch?v=8zO6Wnmp1DU&list=PLx9ewCPgV2w3wNR6KcTDoxrMXKafY7nXJ', 'https://www.youtube.com/watch?v=KlXnApZ8Kq4&list=PL-QvSRz8uhNHt_5IcoQRlkb75crK-NOQ2', 'https://www.youtube.com/watch?v=Tli__NYdSqI', 'https://www.youtube.com/watch?v=8zO6Wnmp1DU&list=PLx9ewCPgV2w3wNR6KcTDoxrMXKafY7nXJ', 'https://www.youtube.com/watch?v=KlXnApZ8Kq4&list=PL-QvSRz8uhNHt_5IcoQRlkb75crK-NOQ2', 
    'https://www.youtube.com/watch?v=bdWUj2NYDYQ', 'https://www.youtube.com/watch?v=Q6cSTBfIGHk', 'https://www.youtube.com/watch?v=OFXC6PDyIBs', 'https://www.youtube.com/watch?v=rA42kDhlMYI', 'https://www.youtube.com/watch?v=ca1kZ4RgZw4', 'https://www.youtube.com/watch?v=-b6ilyqXmTU', 'https://www.youtube.com/watch?v=dCoONMpupl4', 'https://www.youtube.com/watch?v=MvHVzOREGUQ', 'https://www.youtube.com/watch?v=W9tkUovsZJ4', 'https://www.youtube.com/watch?v=sZFdLBrpjGY', 'https://www.youtube.com/watch?v=V3kcs2RNec8', 'https://www.youtube.com/watch?v=neV3EPgvZ3g', 'https://www.youtube.com/watch?v=mSjMsdde-xQ', 'https://www.youtube.com/watch?v=5vV412eHGHc', 'https://www.youtube.com/watch?v=Tl2JICdKvv0', 'https://www.youtube.com/watch?v=NMCgN4QK1Gw', 'https://www.youtube.com/watch?v=Jng4mtb2wIM', 'https://www.youtube.com/watch?v=g8z-qP34-1Y&list=PLlOll-NAMPotWYOYkLqP4u16fERVfF56E', 'https://www.youtube.com/watch?v=8295rOMvtQI&list=PL2tb4KBOS-tlw4Drtem0GCyKkUqfvwzp7', 'https://www.youtube.com/watch?v=DnGdoEa1tPg&list=PL4Li1xClWQsEAg3LcXAJE3VJzzA8seXhD', 
    'https://www.youtube.com/watch?v=5IhwJvvJ2VA&list=PLOARQUBDjA37xE6RX7G5naNjc1sT3p1_Y', 'https://www.youtube.com/watch?v=yQFBKx6eq8s&list=PLAknm6MHSp_Qz7gPCC31LI96HeC8fyYeV', 'https://www.youtube.com/watch?v=uAPUkgeiFVY&list=PL4xqRMQ2GXanzbtvdm2NNpXACQ8MSlVNA', 'https://www.youtube.com/watch?v=pF9buIk57P0', 'https://www.youtube.com/watch?v=YK3zs7EV6Tk&list=PLyl0dE5JtcL8QZQfv0Ji0P5qTqqIwR4lu', 'https://www.youtube.com/watch?v=eM213aMKTHg&list=PLvFYFNbi-IBHkSxfeh_Q-QKGsCRgYd72A', 'https://www.youtube.com/watch?v=SbNfLNCaKqA', 'https://www.youtube.com/watch?v=ulGwHzrKOAU&list=PL3n7zMgQqsHhW_eVY2BZPKx6kyG10FWO1', 'https://www.youtube.com/watch?v=aaYkXg5eCG0', 'https://www.youtube.com/watch?v=VqeGs0K7V2s', 'https://www.youtube.com/watch?v=2Vv-BfVoq4g&list=PL7v1FHGMOadDghZ1m-jEIUnVUsGMT9jbH', 'https://www.youtube.com/watch?v=GsPq9mzFNGY&list=PLic9OgMt4temXortBB2t2pGQN5fkJfrLN', 'https://www.youtube.com/watch?v=xwtdhWltSIg&list=PLinS5uF49IBqNvkIBlLUg8rYPLOb21Z0U', 'https://www.youtube.com/watch?v=bx1Bh8ZvH84&list=PL_5OjOMdSPuxCs6uMRqQ4XemOSyMAupqq', 'https://www.youtube.com/watch?v=QmKxMyKJ2iM'
    'https://www.youtube.com/watch?v=zIrhcTkHX_A&list=PLkfIleCGpZLvw-pYVY9auGcK1A9QVG0Wp', 'https://www.youtube.com/watch?v=SsKT0s5J8ko&list=PL5F_lIxu0wUog5Ea5JvGm2LANEdduU9Rq', 'https://www.youtube.com/watch?v=WABOrIYhR94&list=PLgzTt0k8mXzEaqjkc-CeNg1q5YphbnY2E', 'https://www.youtube.com/watch?v=0xXD9-1mLBY&list=PLL4ZEHd9T5ZYheoYbj6Lr4Sc33HbztjQ7', 'https://www.youtube.com/watch?v=h7l5DF02Q9M', 'https://www.youtube.com/watch?v=3LR9sIVK6TI', 'https://www.youtube.com/watch?v=_ApokDZMDDY', 'https://www.youtube.com/watch?v=EIw8SO6dadQ', 'https://www.youtube.com/watch?v=WgmCloGBBwY', 'https://www.youtube.com/watch?v=xiUhNx24iZs', 'https://www.youtube.com/watch?v=bm0XIfbfKp4', 'https://www.youtube.com/watch?v=pJk1J5jcMZ4', 'https://www.youtube.com/watch?v=Y_7cXDCNKEk', 'https://www.youtube.com/watch?v=4HANIw8ohII', 'https://www.youtube.com/watch?v=9NMtaypXZq8', 'https://www.youtube.com/watch?v=sV2t3tW_JTQ&list=PLx4sLqBJV5wluHJria9hs1oYbv-mH6KV9', 'https://www.youtube.com/watch?v=30FyGBKWWDY', 
    'https://www.youtube.com/watch?v=F2EmooQ1Iag', 'https://www.youtube.com/watch?v=x4ygVwbOyJU', 'https://www.youtube.com/watch?v=gWaat4zZUn8', 'https://www.youtube.com/watch?v=0Hdlh5A6DdY', 'https://www.youtube.com/watch?v=zeqW3apz7rs', 'https://www.youtube.com/watch?v=O2CIAKVTOrc&list=PL64G6j8ePNurWUzrnMGqpIQJ236oAkICT', 'https://www.youtube.com/watch?v=UrIiLvg58SY&list=PLpOehZ0r85ixl-tdCfLqH7JmZe7BwxM2L', 'https://www.youtube.com/watch?v=e1nxy4lmjY4', 'https://www.youtube.com/watch?v=RiSfTyrvJlg&list=PLSTRVL236dhdkXTBPvWe3g3YxOjForMoz', 'https://www.youtube.com/watch?v=rP09GUQFDFk&list=PL64G6j8ePNuqvxRcng0MhfgpY8eTk6-Hb', 'https://www.youtube.com/watch?v=jb6HZa151s8&list=PLenIjFQBKQH4PIiefeQUw_60IWEY1iPrp', 'https://www.youtube.com/watch?v=o_4TRygdoVY&list=PLZBFiRMzR7fLKtPObHWJVAD_-bcG3zh5q', 'https://www.youtube.com/watch?v=zDo0H8Fm7d0&list=PLSgTywHngOwMlZpv8laCA_wTQCC31yDg4', 'https://www.youtube.com/watch?v=Ti_SbTfNI7E', 'https://www.youtube.com/watch?v=rItv9i6c7AY&list=PLLDVfSPfze0vYOLuGg22o3F0ohSmcnOhl', 
    'https://www.youtube.com/watch?v=_WcWHZc8s2I&list=PLh7IzJ3mFYA4KMbZHo93g9_ynU7XWAvQW', 'https://www.youtube.com/watch?v=R-xzfwDAn1I&list=PL7UF9wLCLmQEf3eVfW2ThDgNWKbmVe5qY', 'https://www.youtube.com/watch?v=3XsLBngWPqE']
    webbrowser.open(random.choice(random_playlist))
