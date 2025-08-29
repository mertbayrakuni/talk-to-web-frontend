async function loadBlogs() {
    try {
        const blogResponse = await sendApiRequest('find', 'Blogs');
        const blogs = blogResponse;
        const blogContainer = document.querySelector('#blogCards');
        blogContainer.innerHTML = '';

        const categoriesResponse = await sendApiRequest('find', 'Categories');
        const categories = categoriesResponse;

        for (const blog of blogs) {
            const category = categories.find(cat => cat._id === detectIdType(blog.MainCategory));
            const categoryName = category ? category.Name : 'Kategori Yok';
            
            const formattedName = formatCourseName(blog.BlogName);

            const blogCard = document.createElement('div');
            blogCard.classList.add('col-md-6', 'mb-4');

            blogCard.innerHTML = `
                <div class="card border-0 shadow-sm">
                    <div class="position-relative">
                        <img src="${blog.imageUrl}" class="card-img-top" alt="Blog Post Image">
                        <span class="badge position-absolute top-0 end-0 m-3">${categoryName}</span>
                    </div>
                    <div class="card-body">
                        <div class="mb-3">
                            <div class="d-flex align-items-center text-muted small mb-2">
                                <i class="bi bi-person me-1"></i>
                                <span class="me-3">${blog.WriterName}</span>
                                <i class="bi bi-calendar-event me-1"></i>
                                <span class="me-3">${formatDate(blog.BlogDate)}</span>
                                <i class="bi bi-chat-dots me-1"></i>
                                <span>0 Yorum</span>
                            </div>
                            <h5 class="card-title mb-2">
                                <a href="{{ROOT}}/blog/${formattedName}" class="text-decoration-none">
                                    ${blog.BlogName}
                                </a>
                            </h5>
                        </div>
                    </div>
                </div>
            `;

            // Blog linkine tıklandığında blogId'yi localStorage'a kaydet
            const blogLink = blogCard.querySelector('a');
            blogLink.addEventListener('click', function(event) {
                event.preventDefault(); // Varsayılan davranışı durdur
                const fullHref = `${blogLink.href}?id=${blog._id}`;
                window.location.href = fullHref; // Güncellenmiş href ile yönlendirme
            });

            blogContainer.appendChild(blogCard);
        }
    } catch (error) {
        console.error('Blog verileri yüklenirken bir hata oluştu:', error);
    }
}

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('tr-TR', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

async function loadRecentBlogs() {
    try {
        const response = await sendApiRequest('find', 'Blogs');
        const blogs = response;

        // Blogları ID'lerine göre ters sırayla alıp son iki blogu seçiyoruz
        const recentBlogs = blogs.slice(-2).reverse(); // Son iki blogu al ve ters çevir

        const recentBlogContainer = document.querySelector('#recentBlogContainer');
        recentBlogContainer.innerHTML = '';

        recentBlogs.forEach(blog => {
            const formattedName = formatCourseName(blog.BlogName);
            
            // Blog item elementini oluştur
            const blogItem = document.createElement('li');
            blogItem.classList.add('d-flex', 'mb-3', 'border-bottom', 'pb-3');

            blogItem.innerHTML = `
                <div class="me-3">
                    <a href="{{ROOT}}/blog/${formattedName}" class="image-link">
                        <img src="${blog.imageUrl}" class="img-fluid rounded" alt="Post Thumbnail" width="71" height="71">
                    </a>
                </div>
                <div>
                    <a href="{{ROOT}}/blog/${formattedName}" class="text-link text fw-bold">${blog.BlogName}</a>
                    <p class="text-muted mb-0">Son Eklenen</p>
                </div>
            `;

            // Her iki link için (resim ve başlık) tıklama olayını tanımla
            const links = blogItem.querySelectorAll('a');
            links.forEach(link => {
                link.addEventListener('click', function(event) {
                    event.preventDefault(); // Varsayılan yönlendirmeyi durdur
                    localStorage.setItem('blogId', blog._id); // blogId'yi localStorage'a kaydet
                    window.location.href = `../../../../../talk-to-web-crm/blog/${formattedName}`; // Manuel yönlendirme
                });
            });

            // Oluşturulan blog itemini container'a ekle
            recentBlogContainer.appendChild(blogItem);
        });
    } catch (error) {
        console.error('Son bloglar yüklenirken bir hata oluştu:', error);
    }
}

async function loadCategories() {
    try {
        const response = await sendApiRequest('find', 'Categories'); // Kategorileri al
        const categories = response; // Kategorileri alınan veriden ayıklayın
        const categoryContainer = document.querySelector('#categoryContainer'); // Kategorilerin yer alacağı HTML öğesi

        categoryContainer.innerHTML = ''; // Mevcut içeriği temizle

        categories.forEach(category => {
            const categoryItem = `
                <li class="mb-3">
                    <a href="#" class="text-categories text-decoration-none">${category.Name}</a>
                </li>
            `;
            categoryContainer.innerHTML += categoryItem; // Kategori öğelerini ekle
        });
    } catch (error) {
        console.error('Kategoriler yüklenirken bir hata oluştu:', error);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    loadRecentBlogs();
    loadBlogs();
    loadCategories();
});

function formatCourseName(courseName) {
    return courseName
        .toLowerCase() // Tüm harfleri küçük harfe çevir
        .replace(/ö/g, 'o') // Türkçe karakterleri dönüştür
        .replace(/ü/g, 'u')
        .replace(/ş/g, 's')
        .replace(/ç/g, 'c')
        .replace(/ı/g, 'i')
        .replace(/ğ/g, 'g')
        .replace(/[^a-z0-9\s]/g, '') // Özel karakterleri kaldır
        .replace(/\s+/g, '-') // Boşlukları '-' ile değiştir
        .trim(); // Baş ve sondaki boşlukları kaldır
}
