from PyInquirer import prompt

questions = [
    {
        "type": "list",
        "name": "favorite_language",
        "message": "What is your favorite programming language?",
        "choices": ["Python", "Javascript", "Java", "C++"]
    },
    {
        "type": "checkbox",
        "name": "top_languages",
        "message": "Select you top 5 programming languages",
        "choices": [
            {"name": "Python"},
            {"name": "Java"},
            {"name": "Javascript"},
            {"name": "C++"},
            {"name": "PHP"},
            {"name": "C#"},
            {"name": "Kotlin"},
            {"name": "Perl"},
            {"name": "R"},
        ]
    },
    {
        "type": "confirm",
        "name": "master_programming",
        "message": "Do you want to master programming?",
    }
]

answers = prompt(questions)
print(answers)