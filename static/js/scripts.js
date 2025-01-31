

const searchIcon = document.getElementById('search-icon');
const searchIcon2 = document.getElementById('search-icon2');
const modalElement = document.getElementById('modalElement')

const modalQuestion = new bootstrap.Modal(modalElement);

searchIcon.addEventListener('click', () => {
    modalQuestion.show();
})

searchIcon2.addEventListener('click', (e) => {
    modalQuestion.show();    
})

function toggleForm() {
    let value = document.getElementById('form_card_update').style.display == 'none' ? 'block' : 'none';
    document.getElementById('form_card_update').style.display = value;
    console.log(value)
}
 



