const posts = document.querySelector('.posts')
const post = document.createElement('div')
post.setAttribute('class', 'post')
const title = document.createElement('h2')
const excerpt = document.createElement('p')
const image = document.createElement('img')
posts.append(title)

function get_title(content) {
    return content.Item.post_title.S;
}

function get_excerpt(content) {
    return content.Item.post_excerpt.S;
}

function get_image(content) {
    return content.Item.post_feature.S;
}

let url = 'https://t2646lcfvh.execute-api.us-west-2.amazonaws.com/retrieveTest';
fetch(url)
.then((response) => response.text())
.then((data) => {
    let items = data.split('", "');
    let item = items[0]
    console.log(item);
    let response = JSON.parse(item);

    // post
    posts.append(post);

    // image
    image.src = get_image(response);
    post.append(image);

    // title
    title.textContent = get_title(response);
    post.append(title);

    // excerpt
    excerpt.textContent = get_excerpt(response);
    post.append(excerpt);
})
