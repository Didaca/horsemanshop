const artClassNames = {
    art_img: 'art-img',
    art_name: 'art-name',
    art_type: 'art-type',
    art_price: 'art-price',
    art_color: 'art-color',
    art_size: 'art-size',
    art_par: 'art-desc-par'
}

const art_id = window.location.pathname.split('/')[2]

function CreateArticleDetails(obj) {
    const img_content = document.querySelector('.img-content');
    const art_ul = document.querySelector('.art-ul');
    const art_desc = document.querySelector('.art-desc');

    // create image
    let img = document.createElement('IMG');
    img.classList.add(artClassNames.art_img);
    img.setAttribute('src', obj.image);

    // create article info
    let li_name = document.createElement('LI');
    li_name.classList.add(artClassNames.art_name);
    li_name.textContent = obj.name;

    let li_type = document.createElement('LI');
    li_type.classList.add(artClassNames.art_type);
    li_type.textContent = obj.article_type;

    let li_price = document.createElement('LI');
    li_price.classList.add(artClassNames.art_price);
    li_price.textContent = obj.price;

    let li_color = document.createElement('LI');
    li_color.classList.add(artClassNames.art_color);
    li_color.textContent = obj.color;

    let li_size = document.createElement('LI');
    li_size.classList.add(artClassNames.art_size);
    li_size.textContent = obj.size;

    let h4 = document.createElement('H4');
    h4.classList.add(artClassNames.art_name);
    h4.textContent = obj.name;

    let p = document.createElement('P');
    p.classList.add(artClassNames.art_par);
    p.textContent = obj.description;


    //load all data
    img_content.appendChild(img);

    art_ul.appendChild(li_name);
    art_ul.appendChild(li_type);
    art_ul.appendChild(li_price);
    art_ul.appendChild(li_color);
    art_ul.appendChild(li_size);

    art_desc.appendChild(h4);
    art_desc.appendChild(p);
}


function TakeArticle(id) {
    const {_, article} = api_urls

    return fetch(article(id))
        .then(response => response.json())
}

function GetArticle(art_id) {
    TakeArticle(art_id)
        .then(obj => CreateArticleDetails(obj))
}

GetArticle(art_id)