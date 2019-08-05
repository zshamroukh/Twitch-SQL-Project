from matplotlib import pyplot as plt

# Data From SQL Queries
games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]
viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

# Bar Graph: Featured Games

plt.bar(range(len(games)), viewers, color = 'Mediumslateblue')
plt.title('Top 10 Trending Games: 1/1/15')
plt.legend(['Twitch'])
plt.xlabel('Games')
plt.ylabel('Viewers')
ax = plt.subplot()
ax.set_facecolor('lavender')
ax.set_xticks(range(len(games)))
ax.set_xticklabels(games, rotation = 15)

plt.savefig('bar graph.png', bbox_inches='tight')
plt.show()
plt.clf()

# Pie Chart: League of Legends Viewers' Whereabouts

labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]

colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']

explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

plt.pie(countries, explode = explode, colors = colors, shadow = True,
       startangle = 345, autopct = '%1.0f%%', pctdistance=1.15)
plt.title('League of Legends Viewers by Country')
plt.legend(labels, loc = 'right')

plt.savefig('pie chart.png', bbox_inches='tight')
plt.show()
plt.clf()

# Line Graph: Time Series Analysis

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

y_upper = [x * 1.15 for x in viewers_hour]
y_lower = [x * 0.85 for x in viewers_hour]

plt.plot(hour, viewers_hour)
plt.fill_between(hour, y_lower, y_upper, alpha = 0.2)

plt.title('Time Series')
plt.xlabel('Hour')
plt.ylabel('Viewers Per Hour')
plt.legend(['2015-01-01'])
ax = plt.subplot()
ax.set_xticks(hour)
ax.set_yticks([0, 20, 40, 60, 80, 100, 120])
ax.set_facecolor('seashell')

plt.savefig('line graph.png', bbox_inches='tight')
plt.show()