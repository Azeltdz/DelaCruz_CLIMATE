import sqlite3 # database module (This pyton file is only for the database queries)

# Creating Table
def createTable():
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    # User account table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        real_name TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT (DATETIME('now', '+8 hours'))
    )""")
    # Article table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS article (
        article_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT (DATETIME('now', '+8 hours')),
        FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
        UNIQUE(user_id, title)
    )""")
    # Article bookmark table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS article_bookmark (
        bookmark_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        article_id INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT (DATETIME('now', '+8 hours')),
        FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE,
        FOREIGN KEY (article_id) REFERENCES article(article_id) ON DELETE CASCADE,
        UNIQUE(user_id, article_id)
    )""")
    # Typhoon table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS typhoon (
        typhoon_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        year INTEGER NOT NULL,
        affected TEXT NOT NULL,
        speed REAL NOT NULL,
        created_at TIMESTAMP DEFAULT (DATETIME('now', '+8 hours')),
        FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
        UNIQUE(user_id, name)  
    )""")
    connect.commit()
    connect.close()
# ================================================= INSERTING / POPULATE DATA =================================================
# Populate user Table
def populateuser():
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    # Insert usernames only if they do not already exist
    cursor.execute("""
        INSERT OR IGNORE INTO user (username, password, real_name)
        VALUES
        ('azelt', 'azelt', 'Chester'),
        ('deuz', 'deuz', 'Paul'),
        ('calexia', 'calexia', 'Alejandra'),
        ('nhari', 'nhari', 'Kriskyla'),
        ('hajinomoto', 'hajinomoto', 'Katrine'),
        ('karishe', 'karishe', 'Keil'),
        ('lord zaecks', 'lord zaecks', 'Johann'),
        ('zadkiel', 'zadkiel', 'Jomar'),
        ('sideun', 'sideun', 'Mar Jerome'),
        ('selrahc', 'selrahc', 'Ruwie'),
        ('pearlicious', 'pearlicious', 'Roldan'),
        ('zalvaje', 'zalvaje', 'Marcus'),
        ('dlsknvdsl', 'dlsknvdsl', 'Joseph')
    """)
    connect.commit()
    connect.close()
# Populate Article Table
def populateArticle():
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    # Retrieve only 10 users from user table
    cursor.execute("SELECT user_id FROM user")
    user_ids = cursor.fetchall()
    # Insert Typhoon datas
    cursor.execute(""" 
        INSERT OR IGNORE INTO article (user_id, title, content)
        VALUES
        (?, 'The Impact of Typhoons on Coastal Communities', 'Typhoons cause extensive damage to coastal areas, affecting livelihoods and ecosystems. These storms often result in flooding, destruction of homes, and loss of crops. Communities rely heavily on fishing and agriculture, both of which are severely impacted by such disasters. The rebuilding process can take years, and long-term environmental recovery is often required. Effective preparedness and response systems are crucial for minimizing damages.'),
        (?, 'Preparing for the Next Super Typhoon', 'With the increasing intensity of typhoons, preparedness has become essential. Communities in typhoon-prone areas need to ensure that evacuation plans are in place and that early warning systems are effective. Building resilient infrastructure, such as elevated homes and flood-resistant roads, can reduce the impact of future storms. Government agencies and local communities must collaborate to improve disaster resilience. Public awareness campaigns on typhoon safety can save lives during extreme events.'),
        (?, 'Climate Change and Typhoon Frequency', 'There is a growing concern that climate change is influencing the frequency and severity of typhoons. Rising sea temperatures provide more energy for storm formation, resulting in more intense cyclones. Some regions have observed an increase in the number of typhoons making landfall each year. Scientists are studying the relationship between climate change and typhoon activity to predict future trends and mitigate risks. Understanding this connection is key to adapting to the changing climate.'),
        (?, 'How to Build Resilient Homes', 'Building homes that can withstand typhoon-force winds is crucial for communities in vulnerable areas. Key features include reinforced structures, storm shutters, and elevated foundations. Designing homes with materials that can resist flooding and high winds can prevent significant damage. It is essential to integrate local knowledge and modern engineering practices when constructing disaster-resistant buildings. Proper planning and building codes help reduce casualties and property loss.'),
        (?, 'The Science of Typhoon Formation', 'Typhoons form over warm ocean waters, where heat and moisture are absorbed into the atmosphere. This leads to the development of a low-pressure system that can grow into a powerful cyclone. Wind patterns and ocean currents contribute to the movement and intensity of the storm. Scientists use satellite data and weather models to track these storms and predict their paths. Understanding the science behind typhoon formation helps improve forecasting and preparedness efforts.'),
        (?, 'Emergency Kits: A Lifesaver in Disasters', 'Having an emergency kit ready can make all the difference during a typhoon. Essential items include water, non-perishable food, flashlights, batteries, and first-aid supplies. It’s important to also have tools for communication and shelter, such as a radio and blankets. Kits should be stored in easily accessible locations and checked regularly to ensure items are not expired. Preparing an emergency kit ahead of time saves precious time and ensures safety during a disaster.'),
        (?, 'Economic Impacts of Typhoons', 'Typhoons disrupt local economies by damaging infrastructure, halting trade, and affecting productivity. Agricultural losses, especially in rice and fishing industries, are common following a typhoon. The tourism sector can also be severely affected, with resorts and attractions suffering from the aftermath. Recovery efforts are costly, and it often takes years for the economy to bounce back. Governments and NGOs play a key role in providing financial aid and rebuilding the economy after a disaster.'),
        (?, 'Typhoon Haiyan: Lessons Learned', 'Typhoon Haiyan was one of the strongest storms ever recorded, causing devastation in the Philippines. The disaster highlighted the importance of early warning systems, evacuation planning, and international aid. Many lessons were learned regarding disaster preparedness, with improvements made to response strategies and relief efforts. The storm underscored the need for resilient infrastructure to withstand extreme weather. The experience helped shape future policies and disaster management frameworks.'),
        (?, 'Innovative Weather Forecasting', 'Advancements in weather forecasting technology have improved the accuracy of typhoon predictions. Satellites provide real-time data on storm development, and sophisticated computer models predict their paths. Early warning systems are now capable of giving communities more time to prepare, reducing loss of life and property. Meteorologists are continuously developing better tools to track and study typhoons, providing more reliable forecasts. These innovations are critical in helping authorities make informed decisions during severe weather events.'),
        (?, 'Community-Led Recovery After Typhoons', 'Communities play a vital role in recovery efforts after a typhoon. Local residents often band together to clear debris, rebuild homes, and support one another. In some cases, community-led initiatives are more effective than top-down approaches because they leverage local knowledge and resources. Government and NGO support is essential, but empowering local communities to lead recovery efforts ensures that solutions are tailored to their specific needs. This collective effort promotes long-term resilience and healing.'),
        (?, 'The Role of Ocean Currents in Typhoon Development', 'Ocean currents play a crucial role in the development of typhoons by influencing sea surface temperatures. Warm water is the primary fuel for these storms, providing the necessary heat and moisture. Currents can affect the intensity and path of a typhoon, making forecasting more challenging. Understanding these currents helps meteorologists predict storm behavior and improve early warning systems. This knowledge is vital for preparing coastal regions for typhoon impacts.'),
        (?, 'How Typhoons Affect Marine Ecosystems', 'Typhoons can significantly impact marine ecosystems, particularly coral reefs and coastal habitats. The strong winds and heavy rains cause sediment to be washed into the ocean, reducing water quality. These disturbances can harm marine life, including fish, shellfish, and coral. However, some marine species adapt to these changes, while others face long-term disruptions. Protecting marine ecosystems requires understanding how typhoons alter their dynamics and working to mitigate these impacts.'),
        (?, 'Disaster Relief Efforts After Typhoons', 'Disaster relief efforts are critical in the aftermath of a typhoon, focusing on providing immediate aid and long-term recovery. Humanitarian organizations mobilize to deliver food, water, medical supplies, and shelter to affected populations. Rebuilding infrastructure, such as roads and schools, is a priority in the recovery phase. International aid and government support help communities return to normalcy. Effective coordination between governments, NGOs, and local communities ensures that relief efforts reach those in need.'),
        (?, 'The Psychological Impact of Typhoons on Affected Communities', 'Typhoons leave behind not only physical destruction but also significant psychological trauma. Survivors often experience anxiety, depression, and post-traumatic stress disorder (PTSD). Mental health support is crucial in the aftermath, as communities struggle to cope with the emotional toll. Psychologists and counselors work alongside disaster relief teams to provide essential mental health services. Addressing these psychological impacts is key to the overall recovery process.'),
        (?, 'The Future of Typhoon Prediction Technology', 'Advancements in technology have revolutionized the way we predict typhoons. Modern satellites, radar systems, and computer models allow meteorologists to track storms with unprecedented accuracy. Machine learning and artificial intelligence are also being applied to improve forecasting speed and precision. As these technologies evolve, we can expect more reliable predictions, giving communities more time to prepare. The future of typhoon prediction lies in continuous innovation and the integration of various scientific disciplines.'),
        (?, 'How Typhoons Impact Agriculture and Food Security', 'Typhoons often cause significant damage to crops, leading to food shortages and higher prices. Flooding, soil erosion, and strong winds can destroy rice fields, fruit plantations, and other agricultural resources. The loss of livestock and fisheries also contributes to food insecurity in affected regions. Long-term impacts on agriculture can result in reduced income for farmers and increased dependence on food aid. Governments and organizations must develop strategies to protect agriculture from typhoon damage and ensure food security.'),
        (?, 'The Role of Government in Typhoon Preparedness and Response', 'Governments play a key role in both preparing for and responding to typhoons. Early warning systems, evacuation plans, and infrastructure improvements are all part of government efforts to reduce damage. In the aftermath, governments coordinate disaster relief efforts, mobilizing resources to affected areas. Policies focused on disaster resilience and climate change adaptation are increasingly important as typhoons become more frequent and intense. Effective government leadership is essential for saving lives and minimizing the impact of these storms.'),
        (?, 'The Environmental Costs of Typhoons', 'Typhoons have far-reaching environmental costs that extend beyond the immediate damage. Coastal erosion, deforestation, and loss of biodiversity are common consequences of powerful storms. In some cases, entire ecosystems are destroyed, leaving long-lasting impacts on local wildlife. The cleanup of debris and pollutants also places a heavy burden on natural resources. Minimizing the environmental costs of typhoons requires both preventative measures and extensive post-disaster environmental recovery efforts.'),
        (?, 'The Role of Media in Typhoon Preparedness', 'The media plays a critical role in raising awareness and providing accurate information during typhoon threats. Timely broadcasts help disseminate warnings, evacuation orders, and safety tips to the public. Social media platforms have also become essential for real-time updates and communication between affected communities and authorities. Media outlets must balance the urgency of warnings with responsible reporting to avoid panic. By promoting preparedness and resilience, the media contributes significantly to saving lives.'),
        (?, 'Typhoon-Resistant Infrastructure: Key Considerations', 'Constructing typhoon-resistant infrastructure is vital for communities in typhoon-prone areas. Key considerations include the use of durable materials, elevated structures, and designs that can withstand high winds and heavy rainfall. Coastal defenses, such as sea walls and flood barriers, are also crucial in protecting vulnerable areas. Urban planning and zoning regulations must take into user the risk of typhoons to ensure safe and resilient development. As typhoons become more frequent and intense, the importance of robust infrastructure grows.')
    """, [user_ids[i % 13][0] for i in range(20)])  # Use user_id for each article
    connect.commit()
    connect.close()
# Populate Article Bookmark Table
def populateArticleBookmark():
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    # Retrieve user and article id from the user and article tables
    cursor.execute("SELECT user_id FROM user LIMIT 10")
    user_ids = cursor.fetchall()
    cursor.execute("SELECT article_id FROM article LIMIT 10")
    article_ids = cursor.fetchall()
    # Insert bookmarks directly into the article_bookmark table
    cursor.executemany("""
        INSERT OR IGNORE INTO article_bookmark (user_id, article_id) 
        VALUES (?, ?)
    """, [(user_ids[i][0], article_ids[i][0]) for i in range(10)])
    connect.commit()
    connect.close()
# Populate Typhoon
def populateTyphoon(): 
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    # Retrieve user_ids from the user table
    cursor.execute("SELECT user_id FROM user LIMIT 10")
    user_ids = cursor.fetchall()
    # Insert typhoon data into the typhoon table
    cursor.execute("""
        INSERT OR IGNORE INTO typhoon (user_id, name, year, affected, speed) 
        VALUES
        (?, 'Haiyan (Yolanda)', 2013, 'Philippines, Vietnam, China', 315),
        (?, 'Mangkhut', 2018, 'Philippines, Hong Kong, China, Macau', 305),
        (?, 'Goni (Rolly)', 2020, 'Philippines, Vietnam, Thailand', 315),
        (?, 'Durian (Reming)', 2006, 'Philippines, Vietnam, Thailand', 250),
        (?, 'Ketsana (Ondoy)', 2009, 'Philippines, Vietnam, Cambodia, Laos, Thailand', 175),
        (?, 'Nida (Chedeng)', 2016, 'Philippines, China, Hong Kong', 160),
        (?, 'Choi-wan', 2020, 'Japan, Taiwan, China', 150),
        (?, 'Jebi', 2018, 'Japan', 270),
        (?, 'Bopha (Pablo)', 2012, 'Philippines, Vietnam', 275),
        (?, 'Tembin (Vinta)', 2017, 'Philippines, Malaysia', 170)
    """, (
        user_ids[0][0], user_ids[1][0], user_ids[2][0], user_ids[3][0], user_ids[4][0],
        user_ids[5][0], user_ids[6][0], user_ids[7][0], user_ids[8][0], user_ids[9][0]
    ))
    connect.commit()
    connect.close()
# ================================================= USERNAME TABLE =================================================
# Add username input and password input into database user table
def addNew(username, password, real_name):
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO user (username, password, real_name) VALUES (?, ?, ?)", (username, password, real_name))
    connect.commit()
    connect.close()
# check if username and password exist from database user table
def checkAccount(username, password):
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM user WHERE username=? AND password=?", (username, password))
    acc_result = cursor.fetchone()
    cursor.execute("SELECT username FROM user WHERE username = ?", (username,))
    user_result = cursor.fetchone()
    connect.close()
    return acc_result, user_result
# Show usernames
def showUser():
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    cursor.execute("SELECT username FROM user")
    result = cursor.fetchall()
    connect.close()
    return result
# ================================================= ARTICLE TABLE =================================================
# Add Article to Database
def addArticle(user_id, title, content):
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO article (user_id, title, content) VALUES (?, ?, ?)", (user_id, title, content))
    connect.commit()
    connect.close()
# Fetch Article and the user who posted the article from Database 
def selectArticle():
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    cursor.execute("""SELECT article.article_id, article.title, article.content, article.created_at, user.username 
                        FROM article 
                        JOIN user ON article.user_id = user.user_id
                        ORDER BY article.article_id DESC
                    """)
    result = cursor.fetchall()
    connect.close()
    return result
# Delete Article based on ID from Databasse
def deleteArticle(article_id):
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    cursor.execute("DELETE FROM article WHERE article_id=?", (article_id,))
    connect.commit()
    connect.close()
# Search Article based on ID from Database
def searchArticle(article_id):
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM article WHERE article_id=?", (article_id,))
    result = cursor.fetchall()
    connect.close()
    return result
# UPDATE Article from database
def updateArticle(article_id, title, content):
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE article SET title=?, content=? WHERE article_id=?", (title, content, article_id))
    connect.commit()
    connect.close()
# DROP table to delete all article
def deleteAll():
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    cursor.execute("DELETE FROM article")
    cursor.execute("DELETE FROM article_bookmark")
    connect.commit()
    connect.close()
# ================================================= ARTICLE BOOKMARK TABLE =================================================
# Add Article to Bookmark
def addArticleBookMark(article_id, user_id):
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO article_bookmark (article_id, user_id) VALUES (?, ?)", (article_id, user_id))
    connect.commit()
    connect.close()
# Display Bookmark (SQL query to join article, articleBookmark, and user tables)
def selectArticleBookmark():
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    cursor.execute("""SELECT article.article_id, article.title, article.content, article.created_at, 
                    article_bookmark.bookmark_id, article_bookmark.created_at AS bookmark_created_at, 
                    user.username 
                    FROM article 
                    JOIN article_bookmark ON article.article_id = article_bookmark.article_id
                    JOIN user ON article_bookmark.user_id = user.user_id
                    ORDER BY user.username
                    """)
    bookmark = cursor.fetchall()
    connect.close()
    return bookmark
# Check if article is already bookmarked
def isArticleBookmarked(article_id):
    connect = sqlite3.connect("climate.db") 
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM article_bookmark WHERE article_id=?", (article_id,))
    return cursor.fetchone() is not None
# remove Article Bookmark
def removeArticleBookmark(bookmark_id):
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    cursor.execute("DELETE FROM article_bookmark WHERE bookmark_id=?", (bookmark_id,))
    connect.commit()
    connect.close()
# Delete all bookmark
def deleteAllBookmark():
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    cursor.execute("DELETE FROM article_bookmark")
    connect.commit()
    connect.close()
# ================================================= Typhoon table =================================================
# Add typhoon to database
def addTyphoon(user_id, name, year, affected, speed):
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO typhoon (user_id, name, year, affected, speed) VALUES (?, ?, ?, ?, ?)", (user_id, name, year, affected, speed,))
    connect.commit()
    connect.close()
# Fetch Typhoon from Database
def selectTyphoon(search_query=None):
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    if search_query:
        cursor.execute("""SELECT typhoon_id, typhoon.name, typhoon.year, typhoon.affected, typhoon.speed, typhoon.created_at, user.username
                            FROM typhoon
                            JOIN user ON typhoon.user_id = user.user_id
                            WHERE typhoon.name LIKE ?
                            ORDER BY typhoon.year DESC
                        """, (f"{search_query}%",))
    else:
        cursor.execute("""SELECT typhoon_id, typhoon.name, typhoon.year, typhoon.affected, typhoon.speed, typhoon.created_at, user.username
                            FROM typhoon
                            JOIN user ON typhoon.user_id = user.user_id
                            ORDER BY typhoon.year DESC
                        """)
    typhoonData = cursor.fetchall()
    connect.close()
    return typhoonData
# Delete Article from Databasse
def deleteTyphoon(typhoon_id):
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    cursor.execute("DELETE FROM typhoon WHERE typhoon_id=?", (typhoon_id,))
    connect.commit()
    connect.close()
# Search Typhoon from Database
def searchTyphoon(typhoon_id):
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM typhoon WHERE typhoon_id=?", (typhoon_id,))
    result = cursor.fetchall()
    connect.close()
    return result
# UPDATE Article from database
def updateTyphoon(typhoon_id, name, year, affected, speed):
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE typhoon SET name=?, year=?, affected=?, speed=? WHERE typhoon_id=?", (name, year, affected, speed, typhoon_id))
    connect.commit()
    connect.close()
# DROP table to delete all typhoon
def deleteAllTyphoon():
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    cursor.execute("DELETE FROM typhoon")
    connect.commit()
    connect.close()
# ================================================= COUNT =================================================
# COunt the number of data in a table
def count():
    connect = sqlite3.connect("climate.db")
    cursor = connect.cursor()
    cursor.execute("SELECT COUNT(*) FROM user")
    user = cursor.fetchone()
    cursor.execute("SELECT COUNT(*) FROM article")
    article = cursor.fetchone()
    cursor.execute("SELECT COUNT(*) FROM typhoon")
    typhoon = cursor.fetchone()
    cursor.execute("SELECT COUNT(*) FROM article_bookmark")
    bookmark = cursor.fetchone()
    connect.close()
    total = user + article + typhoon + bookmark
    return total

createTable()
populateuser()
populateArticle()
populateArticleBookmark()
populateTyphoon()