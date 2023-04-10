const posts = document.querySelector('.posts')

function get_title(content) {
    return content.Item.post_title.S;
}

function get_excerpt(content) {
    return content.Item.post_excerpt.S;
}

function get_image(content) {
    return content.Item.post_feature.S;
}

const url = 'https://t2646lcfvh.execute-api.us-west-2.amazonaws.com/retrieveTest';
fetch(url)
    .then((response) => response.text())
    .then((data) => {
        const nosngl = data.replaceAll("'", '"');
        const items = nosngl.split('^*^');
        for (let i = items.length - 1; i >= 0; i--) {
            const post = document.createElement('div')
            post.setAttribute('class', 'post')
            const title = document.createElement('h2')
            const excerpt = document.createElement('p')
            const image = document.createElement('img')
            posts.append(title)
            
            console.log(items[i]);
            const response = JSON.parse(items[i]);

            // post
            posts.appendChild(post);

            // image
            image.src = get_image(response);
            post.append(image);

            // title
            title.textContent = get_title(response);
            post.append(title);

            // excerpt
            excerpt.textContent = get_excerpt(response);
            post.append(excerpt);
        }
    })
