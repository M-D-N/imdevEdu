// Получаем элементы
const openModalBtn = document.getElementById("open-modal");
const modal = document.getElementById("modal");
const quizForm = document.getElementById("quiz-form");
const resultModal = document.getElementById("result");
const score = document.getElementById("score");
const closeResultModalBtn = document.getElementById("close-result-modal");
const closeModalBtn = document.getElementById("modalCloseTestBtn");

// При клике на кнопку открытия модального окна, показываем модальное окно
openModalBtn.addEventListener("click", function () {
    modal.style.display = "block";
});

// При отправке формы с тестом, вычисляем результаты и показываем результаты в модальном окне
quizForm.addEventListener("submit", function (event) {
    event.preventDefault(); // предотвращаем перезагрузку
    let totalScore = 0;

    // Определяем правильные ответы на вопросы
    const correctAnswers = ["a", "a", "a", "a", "a", "a"];

    // Получаем ответы пользователя
    const userAnswers = [
        quizForm.elements["question1"].value,
        quizForm.elements["question2"].value,
        quizForm.elements["question3"].value,
        quizForm.elements["question4"].value,
        quizForm.elements["question5"].value,
        quizForm.elements["question6"].value,
    ];

    // Сравниваем ответы пользователя с правильными ответами
    for (let i = 0; i < userAnswers.length; i++) {
        if (userAnswers[i] === correctAnswers[i]) {
            totalScore++;
        }
    }

    // Выводим результаты в модальное окно
    score.innerHTML = `Вы набрали ${ totalScore } из ${ correctAnswers.length } баллов.`;
    resultModal.style.display = "block";
});

closeModalBtn.addEventListener('click', ()=>{
    modal.style.display = "none";
})

// При клике на кнопку закрытия модального окна с результатами, скрываем его
closeResultModalBtn.addEventListener("click", function () {
    resultModal.style.display = "none";
});
