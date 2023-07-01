function CreateArticlesList(data, name) {

    const { _, article } = urls;

    const aside = document.querySelector('.aside');
    const all_articles = data.filter(a => a.name === name)[0].article_set;

    const ul = document.createElement('UL');
    ul.classList.add(allClassNames.ul_art);

    for(const art of all_articles) {
        const li = document.createElement('LI');
        const a = document.createElement('A');

        li.classList.add(allClassNames.li_art);

        a.setAttribute('href', article(art.id));
        a.classList.add(allClassNames.a_art);
        a.textContent = art.name;

        li.appendChild(a);
        ul.appendChild(li);
    }

    aside.appendChild(ul);
    aside.style.visibility = 'visible';
    aside.style.opacity = 1;

    CloseArticlesEvent(ul);

}


function RemoveArticleList(el) {

    const aside = el.parentElement;
    aside.removeChild(el);
    aside.style.visibility = 'hidden';
    aside.style.opacity = 0;
}


function LoadArticles(n) {
    GetCategories()
        .then(data => CreateArticlesList(data, n));
}
