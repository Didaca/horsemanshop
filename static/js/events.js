window.URLS = {
    allCategories: () => '/shop/categories/'
};


function CreateList(names) {
    const ul = document.querySelector('.ul-categories')

    for (const name of names) {
        let li = document.createElement('LI')

        li.classList.add('li-categories')
        li.textContent = name

        ul.appendChild(li)
    }
}


function LoadData(data) {
    const names = data.map(obj => obj.name)

    CreateList(names);
}


function GetCategories() {

    const { allCategories } = window.URLS;

    fetch(allCategories())
        .then(response => response.json())
        .then(data => LoadData(data))
}

GetCategories();
