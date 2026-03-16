# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  1. The game asked me to enter a number between 1 and 100
  2. There is a box waiting for user input for the number
  3. Beneath the box, there are the buttons "Submit guess", "New game", and "Show hint"
  4. There is a sidebar showing the difficulty selected with the guessing range of each difficulty

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. The guessing range for the normal difficulty is higher than the range for high difficulty
  2. When entering 1 to test the range, the hint told me to go lower. Then I entered 1_000_000, and it still told me to go lower
  3. After finishing the game, I pressed the 'New game button to generate a newer game. Yet, the game did not start over.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Copilot (using the claude model)
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  The AI suggested that the easy difficulty should have the most ammount of attempts.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  The AI kept the number of attempts one over and claimed it had fixed the entire issue

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  By testing it out manually in the game.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  At first, i tested the number of attempts after the first suggestion of AI and it seemed fine. Later on, I caught a bug in the game in which it does not count the number of guesses correctly
- Did AI help you design or understand any tests? How?
  It helped me create a test file and run it to check if the tests are valid. However, one test file claimed to be correct but the logic was still buggy in the code
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  The number keeps changing because the state of having even attempts in the session rewrote over the secret number
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit session state and rerun resetted the secret number due to the number of attempts being resetted
- What change did you make that finally gave the game a stable secret number?
  Removed the option of resetting the secret code every two entries
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I added a 'fix:' before each git message so later on i can navigate between my fixes and features
- What is one thing you would do differently next time you work with AI on a coding task?
  Take its code more seriously, check edge cases that won't break the code in the future
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  AI generated code can be a double edged sword. Either it can produce nearly perfect code that no human can think of, or it can give the most atrocious and buggy code when not prompted correctly.