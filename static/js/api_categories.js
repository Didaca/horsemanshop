const urls = {
    allCategories: () => '/api/categories/',
    article: (id) => `/api/article/${id}/`,
};

const allClassNames = {
    li_cat: 'li-categories',
    ul_art: 'aside-list',
    li_art: 'li-aside',
    a_art: 'a-aside'
}


function CreateList(all) {
    const ul = document.querySelector('.ul-categories');

    for (const art of all) {
        let li = document.createElement('LI');

        li.classList.add(allClassNames.li_cat);
        li.textContent = art.name;

        ShowArticlesEvent(li);

        ul.appendChild(li);
    }
}


function GetCategories() {

    const { allCategories } = urls;

    return  fetch(allCategories())
        .then(response => response.json())

}

function LoadData() {

    GetCategories()
        .then(data => CreateList(data))

}

LoadData()
