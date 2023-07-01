function ShowArticlesEvent(li) {
    li.addEventListener('click', (e) => {
            const n = e.currentTarget.textContent;
            LoadArticles(n);
        })
}

function CloseArticlesEvent(el) {
    window.addEventListener('click', () => {
        RemoveArticleList(el);
        })
}