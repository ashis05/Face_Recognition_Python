#######EXPERIMENTAL FEATURE########
import random

unlisted = []


def send():
    grid = [[' ' for _ in range(15)] for _ in range(15)]
    ans = []
    clues = []
    word_hint_dict = {
    "elephant": "Largest land mammal with a trunk.",
    "camera": "Device used to capture photographs.",
    "journey": "A long trip or adventure.",
    "musician": "Someone who plays musical instruments.",
    "volcano": "A mountain that erupts with lava and ash.",
    "television": "Electronic device for watching shows.",
    "breakfast": "First meal of the day.",
    "wisdom": "Knowledge gained through experience.",
    "butterfly": "Insect known for its colorful wings.",
    "happiness": "Feeling of joy and contentment.",
    "recipe": "Instructions for cooking a dish.",
    "rainbow": "Colorful arc in the sky after rain.",
    "mountain": "Tall landform with peaks.",
    "fireworks": "Explosive displays in the sky.",
    "oxygen": "Essential gas for breathing.",
    "teacher": "Educator in a classroom.",
    "candle": "Wax stick used for illumination.",
    "vacation": "Time off for relaxation and travel.",
    "satellite": "Artificial object orbiting Earth.",
    "guitar": "Stringed musical instrument.",
    "island": "Landmass surrounded by water.",
    "artist": "Creator of visual or performing art.",
    "parade": "Procession of people and floats.",
    "strawberry": "Red fruit often used in desserts.",
    "friendship": "Close and supportive relationship.",
    "bookstore": "Place to buy books.",
    "mysterious": "Enigmatic or hard to understand.",
    "festival": "A joyous celebration or event.",
    "dolphin": "Intelligent marine mammal.",
    "adventure": "Exciting or unusual experience.",
    "chef": "Skilled cook.",
    "curiosity": "Desire to learn and explore.",
    "magician": "Performs tricks and illusions.",
    "river": "Flowing water body.",
    "constellation": "Group of stars forming a pattern.",
    "eclipse": "Celestial event blocking the sun or moon.",
    "tropical": "Relating to warm, humid regions.",
    "history": "Study of past events.",
    "dragonfly": "Insect with transparent wings.",
    "chocolate": "Sweet treat made from cocoa.",
    "celebration": "A festive event or party.",
    "galaxy": "Vast system of stars and planets.",
    "waterfall": "Cascading water over rocks.",
    "painting": "Visual art on canvas.",
    "balloon": "Inflated object for decoration.",
    "architect": "Designer of buildings.",
    "kingdom": "A realm or domain.",
    "astronaut": "Person who travels in space.",
    "spectacular": "Impressive and amazing."
}

    word_list = list(word_hint_dict.keys())
    random.shuffle(word_list)
    word = word_list[:7]

    for index,letters in enumerate(word[0]):
        grid[index][7] = letters
    ans.append(word[0])

    def find_pos(words):
        for row in range(len(grid)):
            for col in range(len(grid[row])):  
                for i in range(len(words)):  
                    if words[i] == grid[row][col]:
                        [cond , dir] = check_space(words[:i][::-1],words[i+1:],row,col)
                        if cond:
                            before = words[:i][::-1]
                            after = words[i+1:]
                            ans.append(words)
                            if dir == 'v':
                                for i in range(len(before)):    
                                    grid[row-i-1][col] = before[i]
                                for i in range(len(after)):
                                    grid[row+i+1][col] = after[i]
                                
                            else:
                                for i in range(len(before)):    
                                    grid[row][col-i-1] = before[i]
                                for i in range(len(after)):
                                    grid[row][col+i+1] = after[i]
                                
                            return
        
        unlisted.append(words)

                        
    def check_space(pre,post,row,col):
        if grid[row - 1][col] == ' ' or grid[row + 1][col] == ' ':
            for i in range(len(pre) + 1):
                if row-i > 0 and col +1 <= 15 and col - 1 >= 0:
                    if grid[row - i - 1][col] != ' ' or grid[row  - i - 1][col- 1] != ' ' or grid[row  - i - 1][col + 1] != ' ':
                        return [False,' ']
                else:
                    return [False,' ']
            for j in range(len(post) + 1):
                if row+j < 14 and col + 1 <= 15 and col - 1 >= 0:
                    if grid[row + j + 1][col] != ' ' or grid[row  + j + 1][col- 1] != ' ' or grid[row  + j + 1][col + 1] != ' ':
                        return [False,' ']
                else:
                    return [False,' ']
            return [True,'v']    
        
        if grid[row][col- 1] == ' ' or grid[row][col + 1] == ' ':
            for i in range(len(pre) + 1):
                if col-i > 0 and row + 1 <= 15 and row - 1 >= 0:
                    if grid[row][col - i - 1] != ' ' or grid[row - 1][col - i - 1] != ' ' or grid[row + 1][col - i -1] != ' ':
                        return [False,' ']
                else:
                    return [False,' ']
            for j in range(len(post) + 1):
                if col+j < 14 and row + 1 <= 15 and row - 1 >= 0:
                    if grid[row][col + j + 1] != ' ' or grid[row - 1][col + j + 1] != ' ' or grid[row + 1][col + j + 1] != ' ':
                        return [False,' ']
                else:
                    return [False,' ']
            return [True,'h']
        return [False," "]

    for i in range(6):
        find_pos(word[i+1])

    failsafe = 0
    while len(ans) < 7:
        try:
            find_pos(random.choice(word_list[8:]))
            failsafe += 1
        except:
            continue
        if failsafe == 30:
            print("failsafe")
            return(send())
    for a in ans:
        clues.append(word_hint_dict[a])

    print(ans)
    return clues,ans,grid
