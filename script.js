const posts = document.querySelector('.posts')
const title = document.createElement('h2')
const excerpt = document.createElement('p')
posts.append(title)

function get_title(content) {
    let id = 'id="title">';
    let len = id.length;
    let start = content.search(id) + len;
    let sub = content.substring(start+len);
    let end = sub.search('<') + start + len;
    return content.substring(start, end);
}

function get_excerpt(content) {
    let id = 'id="excerpt">';
    let len  = id.length;
    let start = content.search(id) + len;
    let sub = content.substring(start+len);
    let end = sub.search('<') + start + len;
    return content.substring(start, end);
}

console.log('.' + location.pathname);

let url = './posts/2021/06/27/The-Great-Yeast-Failure-of-2021.html';
fetch(url)
.then((response) => response.text())
.then((data) => {
    // title
    title.textContent = get_title(data);
    posts.append(title);

    // excerpt
    excerpt.textContent = get_excerpt(data);
    posts.append(excerpt);

    // image
})
