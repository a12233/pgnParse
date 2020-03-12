from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

def main(url, moves):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(str(url))
    arr = []
    for i in range(int(moves)*2):
        elem = driver.find_element_by_id("mv"+str(i))
        arr.append((elem.text))
    print(" ".join(arr))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])



    # <div id="olga-data" sessid="1" color_light="#FFCC99" color_dark="#CC9966" labels="Y" pgn="[Event &quot;Spassky - Fischer World Championship Match&quot;]
    # [Site &quot;Reykjavik ISL&quot;]
    # [Date &quot;1972.07.20&quot;]
    # [EventDate &quot;?&quot;]
    # [Round &quot;5&quot;]
    # [Result &quot;0-1&quot;]
    # [White &quot;Boris Spassky&quot;]
    # [Black &quot;Robert James Fischer&quot;]
    # [ECO &quot;E41&quot;]
    # [WhiteElo &quot;?&quot;]
    # [BlackElo &quot;?&quot;]
    # [PlyCount &quot;54&quot;]
    #
    # 1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Nf3 c5 5. e3 Nc6 6. Bd3 Bxc3+ 7. bxc3 d6 8. e4 e5 9. d5 Ne7 10. Nh4 h6 11. f4 Ng6 12. Nxg6 fxg6 13. fxe5 dxe5 14. Be3 b6 15. O-O O-O 16. a4 a5 17. Rb1 Bd7 18. Rb2 Rb8 19. Rbf2 Qe7 20. Bc2 g5 21. Bd2 Qe8 22. Be1 Qg6 23. Qd3 Nh5 24. Rxf8+ Rxf8 25. Rxf8+ Kxf8 26. Bd1 Nf4 27. Qc2 Bxa4 0-1" ratio="80" notes="[]">
    # </div>