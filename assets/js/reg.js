// POST ЗАПРОС 

// Создаем переменную которая будет равна ссылку с источника данных то есть ссылка от куда мы будет получать данные через метод GET POST
const requestURL = 'https://jsonplaceholder.typicode.com/users';

// Создается функция для отправки запроса на ссылку выше 
// Задаем параметры к функции method, url, body - для POST запросов body необходим
function sendRequest(method, url, body = null){

    // Задаем переменную headers типа данных для подключения объекта конфигурации ниже
    const headers = {
        'Content-Type':'application/json'
    };
    
    // Используем API FETCH() - принимает url так же автоматом возвращает Promise нам 
    return fetch(url, {
        // Передаем объект конфигурации где указываем парметры такие как:
        method: method,
        body: JSON.stringify(body), // Body ппередаем в типе JSON.stringify что бы превратить наши данные в тип строки
        // Для указания тип header (как в xhr запросе 'Content-Type', 'application/json')
        headers: headers 
    })

        // Указываем после запроса fetch(url) с ссылкой что нам возвращать от туда
        .then(response => {

            // Просим данные возвращать нам в виде json объекта 
            return response.json()
        })
};

// Создаем объект который хотим передать серверу через запрос POST (обязательно объект должен идти после функции отправки sendRequest()!!!!)
const body = {
    login: '',
    password: ''
};

const inputLogin = document.getElementById('login');
const inputPass = document.getElementById('password');
const loginBtn = document.getElementById('loginBtn')



// Вызываем саму функцию указываею нужные параметры method, URL 

loginBtn.addEventListener('click', ()=>{
    
    body.login = inputLogin.value;
    body.password = inputPass.value;

    sendRequest('POST', requestURL, body)
        .then(data => console.log(data))
        .catch(err => console.log(err))
    
    console.log(body.login + ' ' + body.password);
});
