document.addEventListener('DOMContentLoaded', async function() {
    const urlParams = new URLSearchParams(window.location.search);
    const blogId = urlParams.get('id'); // URL'deki id parametresi

    if (blogId) {
        try {
            // blogId'nin integer tipinde olduğundan emin olun
            const response = await sendApiRequest('findOne', 'Blogs', { '_id': detectIdType(blogId) });
            
            if (response) {
                const blog = response;
                document.querySelector('.bi-person').innerText = blog.WriterName;
                /*document.querySelector('.bi-calendar').innerText = new Date(blog.date).toLocaleDateString();*/
                document.getElementById('banner-title').innerText = blog.BlogName;
                document.getElementById('site-title').innerText = blog.BlogName;
                document.getElementById('main-title').innerText = blog.BlogName;
                document.getElementById('blog-content').innerHTML = blog.Content;
                document.getElementById('blog-img').src = blog.imageUrl;
            } else {
                console.error('Blog not found or invalid response format');
            }
        } catch (error) {
            console.error('Error fetching blog data:', error);
        }
    } else {
        console.error('No blogId found in localStorage');
    }
});
