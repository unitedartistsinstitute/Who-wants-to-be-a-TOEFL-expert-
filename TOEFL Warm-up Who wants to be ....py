Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Who Wants to Be a TOEFL Expert?</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-image: url('https://upload.wikimedia.org/wikipedia/en/8/8d/WWTBAM_Logo.png');
            background-size: cover;
            background-position: center;
            color: #fff;
            text-align: center;
        }
        .container {
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: rgba(0, 0, 0, 0.8);
            border-radius: 10px;
        }
        .question {
            font-size: 24px;
            margin-bottom: 20px;
            padding: 15px;
            background-color: rgba(70, 130, 180, 0.6);
            border-radius: 5px;
        }
        .answers {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }
        .answer {
            padding: 15px;
            border: 2px solid #fff;
            border-radius: 5px;
            cursor: pointer;
            background-color: rgba(70, 130, 180, 0.4);
            transition: background-color 0.3s;
        }
        .answer:hover {
            background-color: rgba(70, 130, 180, 0.6);
        }
        .answer.correct {
            background-color: rgba(0, 255, 0, 0.6);
        }
        .answer.wrong {
            background-color: rgba(255, 0, 0, 0.6);
        }
        .lifeline {
            margin-top: 20px;
            margin-right: 10px;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .lifeline:disabled {
            background-color: #666;
            cursor: not-allowed;
        }
        .next-button {
            display: none;
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .score {
            font-size: 20px;
            margin: 15px 0;
            color: #ffd700;
        }
        .signature {
            margin-top: 30px;
            font-size: 14px;
            color: #ccc;
        }
        .signature a {
            color: #007bff;
            text-decoration: none;
        }
        .signature a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Who Wants to Be a TOEFL Expert?</h1>
        <div class="score" id="score">Current Prize: $0</div>
        <div class="question" id="question"></div>
        <div class="answers">
            <div class="answer" id="answer1" onclick="checkAnswer(0)"></div>
            <div class="answer" id="answer2" onclick="checkAnswer(1)"></div>
            <div class="answer" id="answer3" onclick="checkAnswer(2)"></div>
            <div class="answer" id="answer4" onclick="checkAnswer(3)"></div>
        </div>
        <button class="lifeline" id="lifeline5050" onclick="useLifeline('5050')">50:50</button>
        <button class="lifeline" id="lifelineAudience" onclick="useLifeline('audience')">Ask the Audience</button>
        <button class="lifeline" id="lifelinePhone" onclick="useLifeline('phone')">Phone a Friend</button>
        <button class="next-button" id="nextButton" onclick="nextQuestion()">Next Question</button>
        
        <div class="signature">
            &copy; 2025 Daniel Rojas | &#9993; <a href="mailto:unitedartistsinstitute@gmail.com">unitedartistsinstitute@gmail.com</a>
        </div>
    </div>

    <script>
        const questions = [
            {
                question: "What is the primary purpose of a TOEFL Reading passage?",
                answers: [
                    "To test vocabulary only",
                    "To assess academic reading comprehension",
                    "To evaluate creative writing skills",
                    "To test conversational English"
                ],
                correct: 1,
                money: 100
            },
            {
                question: "How many main sections does the TOEFL exam have?",
                answers: [
                    "2 sections",
                    "3 sections",
                    "4 sections",
                    "5 sections"
                ],
                correct: 2,
                money: 200
            },
            {
                question: "Which section includes integrated tasks combining multiple skills?",
                answers: [
                    "Reading only",
                    "Listening only",
                    "Speaking and Writing",
                    "All sections"
                ],
                correct: 2,
                money: 300
            },
            {
                question: "What is the total possible TOEFL score?",
                answers: [
                    "0-90",
                    "0-100",
                    "0-120",
                    "0-150"
                ],
                correct: 2,
                money: 500
            },
            {
                question: "How many academic passages are typically in the Reading section?",
                answers: [
                    "1-2",
                    "3-5",
                    "5-6",
                    "7-8"
                ],
                correct: 1,
                money: 1000
            },
            {
                question: "What is the approximate total test duration?",
                answers: [
                    "2 hours",
                    "3 hours",
                    "4 hours",
                    "5 hours"
                ],
                correct: 2,
                money: 2000
            },
            {
                question: "Which skill is NOT tested in the TOEFL exam?",
                answers: [
                    "Speaking",
                    "Listening",
                    "Translation",
                    "Writing"
                ],
                correct: 2,
                money: 4000
            },
            {
                question: "How long are TOEFL scores valid?",
                answers: [
                    "1 year",
                    "2 years",
                    "5 years",
                    "Permanently"
                ],
                correct: 1,
                money: 8000
            },
            {
                question: "Which section allows note-taking?",
                answers: [
                    "Reading",
                    "Listening",
                    "Speaking",
                    "All sections"
                ],
                correct: 3,
                money: 16000
            },
            {
                question: "What type of English does TOEFL primarily assess?",
                answers: [
                    "British English",
                    "Australian English",
                    "Academic English",
                    "Colloquial English"
                ],
                correct: 2,
                money: 32000
            },
            {
                question: "Which organization administers the TOEFL?",
                answers: [
                    "British Council",
                    "Cambridge University",
                    "ETS (Educational Testing Service)",
                    "IDP Education"
                ],
                correct: 2,
                money: 64000
            },
            {
                question: "How many writing tasks are there?",
                answers: [
                    "1",
                    "2",
                    "3",
                    "4"
                ],
                correct: 1,
                money: 125000
            },
            {
                question: "Which section includes conversations and lectures?",
                answers: [
                    "Reading",
                    "Listening",
                    "Speaking",
                    "Writing"
                ],
                correct: 1,
                money: 250000
            },
            {
                question: "What is the format of most TOEFL questions?",
                answers: [
                    "Essay writing",
                    "Multiple choice",
                    "Short answer",
                    "Diagram labeling"
                ],
                correct: 1,
                money: 500000
            },
            {
                question: "How much does the exam cost?",
                answers: [
                    "USD $150",
                    "Varies upon location",
                    "USD $180",
                    "USD $250"
                ],
                correct: 1,
                money: 1000000
            },
            {
                question: "What is unique about TOEFL Speaking tasks?",
                answers: [
                    "Done in pairs",
                    "Recorded responses",
                    "Face-to-face interview",
                    "Group discussions"
                ],
                correct: 1,
                money: 2500000
            },
            {
                question: "Which resource is official TOEFL preparation material?",
                answers: [
                    "Cambridge IELTS books",
                    "ETS Official Guide",
                    "Barron's SAT Prep",
                    "Oxford Dictionary"
                ],
                correct: 1,
                money: 5000000
            },
            {
                question: "What is the maximum section score?",
                answers: [
                    "20 points",
                    "25 points",
                    "30 points",
                    "35 points"
                ],
                correct: 2,
                money: 7500000
            },
            {
                question: "Which feature characterizes TOEFL Reading passages?",
                answers: [
                    "Fictional stories",
                    "Academic topics",
                    "Newspaper articles",
                    "Poetry analysis"
                ],
                correct: 1,
                money: 10000000
            },
            {
                question: "What is required for the Writing section?",
                answers: [
                    "Handwritten essays",
                    "Typed responses",
                    "Bullet point lists",
                    "Creative drawings"
                ],
                correct: 1,
                money: 50000000
            }
        ];

        let currentQuestion = 0;
        let lifelinesUsed = { '5050': false, 'audience': false, 'phone': false };
        let currentMoney = 0;

        function loadQuestion() {
            const question = questions[currentQuestion];
            document.getElementById('question').textContent = question.question;
            
            const answers = document.querySelectorAll('.answer');
            answers.forEach((answer, index) => {
                answer.textContent = question.answers[index];
                answer.classList.remove('correct', 'wrong');
                answer.style.visibility = 'visible';
            });
            
            document.getElementById('nextButton').style.display = 'none';
            document.getElementById('score').textContent = `Current Prize: $${currentMoney}`;
        }

        function checkAnswer(selected) {
            const correct = questions[currentQuestion].correct;
            const answers = document.querySelectorAll('.answer');
            
            answers[selected].classList.add(selected === correct ? 'correct' : 'wrong');
            if (selected === correct) {
                currentMoney = questions[currentQuestion].money;
                document.getElementById('score').textContent = `Current Prize: $${currentMoney}`;
            } else {
                currentMoney = 0;
                document.getElementById('score').textContent = `Game Over! Final Prize: $0`;
                endGame();
            }
            
            document.getElementById('nextButton').style.display = 'block';
        }

        function useLifeline(lifeline) {
            const question = questions[currentQuestion];
            const correct = question.correct;
            const answers = document.querySelectorAll('.answer');

            if (lifeline === '5050' && !lifelinesUsed['5050']) {
                lifelinesUsed['5050'] = true;
                const incorrectAnswers = [0, 1, 2, 3].filter(i => i !== correct);
                incorrectAnswers.slice(0, 2).forEach(index => {
                    answers[index].style.visibility = 'hidden';
                });
            } else if (lifeline === 'audience' && !lifelinesUsed['audience']) {
                lifelinesUsed['audience'] = true;
                alert(`The audience suggests answer ${String.fromCharCode(65 + correct)}!`);
            } else if (lifeline === 'phone' && !lifelinesUsed['phone']) {
                lifelinesUsed['phone'] = true;
                alert(`Your TOEFL expert friend suggests answer ${String.fromCharCode(65 + correct)}!`);
            }

            document.getElementById(`lifeline${lifeline}`).disabled = true;
        }
             function useLifeline(lifeline) {
            const question = questions[currentQuestion];
            const correct = question.correct;
            const answers = document.querySelectorAll('.answer');

            if (lifeline === '5050' && !lifelinesUsed['5050']) {
                lifelinesUsed['5050'] = true;
                const incorrectAnswers = [0, 1, 2, 3].filter(i => i !== correct);
                incorrectAnswers.slice(0, 2).forEach(index => {
                    answers[index].style.visibility = 'hidden';
                });
            } else if (lifeline === 'audience' && !lifelinesUsed['audience']) {
...                 lifelinesUsed['audience'] = true;
...                 alert(`The audience suggests answer ${String.fromCharCode(65 + correct)}!`);
...             } else if (lifeline === 'phone' && !lifelinesUsed['phone']) {
...                 lifelinesUsed['phone'] = true;
...                 alert(`Your TOEFL expert friend suggests answer ${String.fromCharCode(65 + correct)}!`);
...             }
... 
...             // Corrected line to handle capitalization of lifeline IDs
...             document.getElementById(`lifeline${lifeline.charAt(0).toUpperCase() + lifeline.slice(1)}`).disabled = true;
...         }
...         function nextQuestion() {
...             currentQuestion++;
...             if (currentQuestion < questions.length) {
...                 loadQuestion();
...             } else {
...                 endGame();
...             }
...         }
... 
...         function endGame() {
...             const container = document.querySelector('.container');
...             container.innerHTML = `
...                 <h1>Game Over!</h1>
...                 <div class="score">Final Prize: $${currentMoney}</div>
...                 <p>Congratulations on completing the TOEFL Millionaire Challenge!</p>
...                 <div class="signature">
...                     &copy; 2025 Daniel Rojas | &#9993; <a href="mailto:unitedartistsinstitute@gmail.com">unitedartistsinstitute@gmail.com</a>
...                 </div>
...             `;
...         }
... 
...         window.onload = loadQuestion;
...     </script>
... </body>
