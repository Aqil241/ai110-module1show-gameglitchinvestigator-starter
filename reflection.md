# 🔍 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first examined the game, I found several bugs in the starter code. One bug was that when a guess was too high, the game told the player to go higher, and when a guess was too low, it told the player to go lower. Another bug was that the secret number was converted from an integer to a string on every other attempt, which caused inconsistent comparisons. I also noticed that the original tests only checked the outcome string even though `check_guess()` returned both an outcome and a message.

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|---|---|---|---|
| Guess 60, secret 50 | Return "Too High" and tell the player to go lower | Returned "Too High" but told the player to go higher | No console error |
| Guess 40, secret 50 | Return "Too Low" and tell the player to go higher | Returned "Too Low" but told the player to go lower | No console error |
| Guess on an even-numbered attempt | Compare the guess and secret as integers | The secret was converted into a string | Could cause a TypeError during comparison |

---

## 2. How did you use AI as a teammate?

I used Claude Code as my AI coding assistant during this project. One suggestion I accepted was to move the game logic from `app.py` into `logic_utils.py` and correct the reversed high and low hint messages inside `check_guess()`. This suggestion was correct because the game logic did not depend on the Streamlit UI, and the corrected hints now tell a player with a high guess to go lower and a player with a low guess to go higher. I verified the changes by updating the tests and running `python -m pytest`, which resulted in all three tests passing.

One suggestion I did not follow exactly was removing the original buggy code immediately. I chose to keep the original code commented out temporarily and added `# FIXME` and `# FIX` comments so I could clearly document where the bug was and how it was repaired. I verified that my version still worked by running the automated tests after the change and confirming that all three tests passed.

---

## 3. Debugging and testing your fixes

I decided that a bug was fixed only after the corrected behavior was verified with automated tests. I updated `tests/test_game_logic.py` so it checked both the outcome and the hint message returned by `check_guess()`. I tested a winning guess, a guess that was too high, and a guess that was too low by running `python -m pytest`, and all three tests passed. AI helped me understand that the tests originally expected only a string even though the function actually returned a tuple containing both the outcome and the message. I also ran the game with `streamlit run app.py` and manually verified that guesses above the secret told the player to go lower and guesses below the secret told the player to go higher.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the Python script when the user interacts with widgets such as buttons or text inputs. Because the script reruns, `st.session_state` is used to preserve important values between those reruns. In this project, values such as the secret number, score, attempts, game status, and history were stored in session state so they were not recreated every time the page updated. I also learned that state-related bugs can be confusing because the code may rerun many times even though it looks like a normal Python script.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse in future projects is writing or updating tests immediately after fixing a bug so I can prove that the behavior is correct. I also want to use smaller and more specific prompts when working with AI instead of asking it to change many parts of a program at once. This project showed me that AI-generated code should still be reviewed carefully because the code can run while still containing logical mistakes. In future projects, I will treat AI suggestions as something to inspect and test rather than automatically accept.