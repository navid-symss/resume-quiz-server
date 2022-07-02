from fastapi import FastAPI, Response
from typing import Callable
app = FastAPI()


def solve_puzzle(puzzle: str):
    letters_default='ABCD'
    letters = list(letters_default)
    
    for letter_row, line in zip(letters_default, puzzle.split("\n")[2:]):
        for letter_col, sign in zip(letters_default, line[1:]):
            val_row = letters.index(letter_row)
            val_col = letters.index(letter_col)
            print(f'{letter_row}{val_row}-{letter_col}{val_col}-{sign}')
            if sign == "<" and val_row>val_col:
                letters.pop(val_row)
                letters.insert(val_col,letter_row)
            elif sign == ">" and val_row<val_col:
                letters.pop(val_row)
                letters.insert(val_col+1,letter_row)
    result = f" {''.join(letters_default)}"
    for letter_row in letters_default:
        result+=f'\n{letter_row}'
        val_row = letters.index(letter_row)
        for letter_col in letters_default:
            val_col = letters.index(letter_col)
            if val_row > val_col:
                result+='>'
            elif val_row<val_col:
                result+='<'
            else:
                result+='='
    return result


@app.get("/test")
async def root(q: str, d: str):
    answers = {
        "Ping": "OK",
        "Years": "10",
        "Position": "Senior Developer",
        "Email Address": "a.d.symss@gmail.com",
        "Phone": "+905528811183",
        "Referrer": "I was referred by turing team",
        "Name": "Navid Kovashimeh",
        "Status": "I have a Turkish residence card.  So I'm allowed to work with US and there is no problem with US law.",
        "Degree": "Mechanical Engineering at Sharif University Of Technology (October 2009 - September 2014)",
        "Resume": "https://matching.turing.com/pdf/?url=https://matching.turing.com/developer-resume/e4c81687bf40106c6728e60803edc208ec9bc10aa23d78/pdf",
        "Source": "https://github.com/navid-symss/resume-quiz-server.git",
        "Puzzle": solve_puzzle,
    }
    ans = answers.get(q, None)
    if ans:
        if isinstance(ans, Callable):
            ans = ans(d)
        return Response(ans)
    else:
        print(q, "|", d)
