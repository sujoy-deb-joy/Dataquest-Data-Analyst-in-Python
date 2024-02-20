row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

fb_rating_data = [row_1[0], row_1[3], row_1[-1]]
insta_rating_data = [row_2[0], row_2[3], row_2[-1]]
minecraft_rating_data = [row_5[0], row_5[3], row_5[4]] # row_5[4] is the same as row_5[-1]

total_rating = fb_rating_data[2] + insta_rating_data[2] + minecraft_rating_data[2]
average_rating = total_rating / 3