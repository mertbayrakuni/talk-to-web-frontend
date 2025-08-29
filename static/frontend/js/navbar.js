const startTime = Date.now();


async function initializePage() {
    try {
        const headerResponse = await fetch('{{ROOT}}/CrmProject/Navbar/Html/Header.html');
        const headerText = await headerResponse.text();
        const parser = new DOMParser();
        const Hdoc = parser.parseFromString(headerText, 'text/html');
        const navbar = Hdoc.getElementById('header-div');
        const footer = Hdoc.getElementById('footer-div')

        document.getElementById('header-cont').innerHTML = navbar.outerHTML;
        document.getElementById('footer-cont').innerHTML = footer.outerHTML

    } catch (error) {
        console.error('Error initializing page:', error);
    }
}

document.addEventListener('DOMContentLoaded', async function () {
    await initializePage();
    CardData();
    
    const menuButton = document.querySelector('.icon-menu-button');
    const backButton = this.getElementById('menuBack');
    const header = document.getElementById('header-div');
    const offcanvas = document.querySelector('.offcanvas-custom');
    const blogCardElements = document.querySelectorAll('.blog-section .card');
    const categoryCounts = {};
    const contactForm = document.getElementById('contactForm');
    const successMessage = document.getElementById('successMessage');
    const statsSuccessMessage = document.createElement('div');
    const menuButtonIcon = document.getElementById('menuButtonIcon');
    const menuButtonText = document.getElementById('menuButtonText');
    const CourseSelect = document.getElementById('educationForm')
    const container = document.getElementById('MainCourses');
    
    CourseSelect ? PopulateCourses(): "" ;
    container ? populateMainEducations():""; 
    
    if (statsForm) {
        statsSuccessMessage.className = 'mt-3 text-success';
        statsSuccessMessage.style.display = 'none';
        statsSuccessMessage.textContent = 'Başarılı! Bilgileriniz alınmıştır.';
        statsForm.parentNode.appendChild(statsSuccessMessage);
    }
    
    document.getElementById('menuButton').addEventListener('click',function(){
        if(document.getElementById('offcanvasScrolling').classList.contains('show')){
            document.getElementById('menuButtonText').innerText='MENÜ'
        } else {
            document.getElementById('menuButtonText').innerText='KAPAT'   
        }
    })

    if (contactForm) {
        contactForm.addEventListener('submit', function (event) {
            event.preventDefault();

            const nameInput = document.getElementById('nameInput').value.trim();
            const phoneInput = document.getElementById('phoneInput').value.trim();

            if (nameInput && phoneInput) {
                successMessage.style.display = 'block';

                contactForm.reset();

                setTimeout(function () {
                    successMessage.style.display = 'none';
                }, 5000);
            }
        });
    }

    if (statsForm) {
        statsForm.addEventListener('submit', function (event) {
            event.preventDefault();

            const nameInput = statsForm.querySelector('input[placeholder="Ad Soyad"]').value.trim();
            const phoneInput = statsForm.querySelector('input[placeholder="Telefon"]').value.trim();

            if (nameInput && phoneInput) {
                statsSuccessMessage.style.display = 'block';

                statsForm.reset();

                setTimeout(function () {
                    statsSuccessMessage.style.display = 'none';
                }, 5000);
            }
        });
    }

    offcanvas.addEventListener('show.bs.offcanvas', function () {
        if (menuButtonIcon) {
            menuButtonIcon.classList.remove('bi-list');
            menuButtonIcon.classList.add('bi-x');
        }
    });

    offcanvas.addEventListener('hide.bs.offcanvas', function () {
        if (menuButtonIcon) {
            menuButtonIcon.classList.remove('bi-x');
            menuButtonIcon.classList.add('bi-list');
        }
    });

    blogCardElements.forEach(function (card) {
        const badge = card.querySelector('.badge');
        if (badge) {
            const category = badge.textContent.trim();
            if (categoryCounts[category]) {
                categoryCounts[category]++;
            } else {
                categoryCounts[category] = 1;
            }
        }
    });

    const categoryListItems = document.querySelectorAll('.side-content .text-categories');

    categoryListItems.forEach(function (item) {
        const categoryName = item.textContent.split(' (')[0].trim();
        if (categoryCounts[categoryName]) {
            item.textContent = `${categoryName} (${categoryCounts[categoryName]})`;
        }
    });

    function adjustOffcanvas() {
        const headerHeight = header.offsetHeight;
        offcanvas.style.top = `${headerHeight}px`;
        offcanvas.style.height = `calc(100% - ${headerHeight}px)`;
    }

    adjustOffcanvas();
    window.addEventListener('resize', adjustOffcanvas);

    if (!localStorage.getItem('lastSelectedSection')) {
        localStorage.setItem('lastSelectedSection', 'educations');
    }
    setActiveSection(localStorage.getItem('lastSelectedSection'));

    let currentIndex = 0;
    const wrapper = document.querySelector('.testimonial-wrapper');
    
    if(wrapper){
        const items = document.querySelectorAll('.testimonial-item');
        const totalItems = items.length;
        let visibleItems = window.innerWidth <= 768 ? 1 : (window.innerWidth <= 991 ? 2 : 4);
        let itemWidth = 100 / visibleItems;
        
        for (let i = 0; i < visibleItems; i++) {
            wrapper.appendChild(items[i].cloneNode(true));
            wrapper.insertBefore(items[totalItems - 1 - i].cloneNode(true), items[0]);
        }

        wrapper.style.transform = `translateX(-${itemWidth * visibleItems}%)`;
        setInterval(slideTestimonials, 3000);
    
        function slideTestimonials() {
            currentIndex++;
            wrapper.style.transition = 'transform 0.5s ease-in-out';
            wrapper.style.transform = `translateX(-${(currentIndex + visibleItems) * itemWidth}%)`;
    
            if (currentIndex >= totalItems) {
                setTimeout(() => {
                    currentIndex = 0;
                    wrapper.style.transition = 'none';
                    wrapper.style.transform = `translateX(-${itemWidth * visibleItems}%)`;
                }, 500);
            }
        }
    }
    
    if(wrapper){
        window.addEventListener('resize', function () {
            visibleItems = window.innerWidth <= 768 ? 1 : (window.innerWidth <= 991 ? 2 : 4);
            itemWidth = 100 / visibleItems;
            wrapper.style.transform = `translateX(-${(currentIndex + visibleItems) * itemWidth}%)`;
        });    
    }
    

    function adjustOffcanvasForMobile() {
        const offcanvasContent = document.getElementById('offcanvas-content');
        const offcanvasHeader = document.getElementById('offcanvas-header');

        if (window.innerWidth <= 768) {
            offcanvasContent.classList.remove('col-10');
            offcanvasContent.classList.add('d-none');
            offcanvasHeader.classList.remove('col-2');
            
            document.querySelector('.btn-student-mobile').parentElement.parentElement.classList.remove('d-none')
            
            document.getElementById("homeLink").classList.add('d-none')

            document.querySelectorAll('.header-link').forEach((element) => {
                element.addEventListener('click', function (e) {
                    e.preventDefault();
                    const selectedSection = element.getAttribute('data-content');
                    if (selectedSection) {
                        localStorage.setItem('lastSelectedSection', selectedSection);
                        setActiveSection(selectedSection);

                        document.getElementById('offcanvas-content').classList.remove('d-none');
                        setTimeout(() => {
                            document.getElementById('offcanvas-content').classList.add('show');
                        }, 1);
                        menuButton.classList.add('d-none');
                        backButton.classList.remove('d-none');
                    }
                });
            });

            backButton.addEventListener('click', function () {
                document.getElementById('offcanvas-content').classList.remove('show');
                setTimeout(() => {
                    document.getElementById('offcanvas-content').classList.add('d-none');
                }, 350);
                menuButton.classList.remove('d-none');
                backButton.classList.add('d-none');
            });
        } else {
            offcanvasContent.classList.add('col-10');
            offcanvasContent.classList.remove('col', 'd-none');
            offcanvasHeader.classList.add('col-2');
            offcanvasHeader.classList.remove('col');
        }
    }

    adjustOffcanvasForMobile();
    window.addEventListener('resize', adjustOffcanvasForMobile);
    
    document.addEventListener('scroll', function () {
        const topHeader = document.querySelector('.top-header');
        const links = topHeader.querySelectorAll('a');
        const navbar = document.querySelector('.navbar-custom');
        const brand = document.querySelector('.navbar-brand');
        const homeButtons = document.querySelectorAll('.icon-home-button');
        const logos = document.querySelectorAll('#navbarLogo, #navbarLogoMobile');
        const houseIcons = document.querySelectorAll('.house-icon');
        const logoText = document.querySelectorAll('.logo-font-style');
    
        if (window.scrollY > 50) {
            topHeader.classList.add('scrolled');
            document.querySelector('.info-text').classList.add('scrolled')
            links.forEach(link => {
                if (link.classList.contains('youtube')) {
                    link.style.color = '#FF0000'; // YouTube kırmızı
                } else if (link.classList.contains('instagram')) {
                    link.style.color = '#C13584'; // Instagram pembe
                } else if (link.classList.contains('linkedin')) {
                    link.style.color = '#0077B5'; // LinkedIn mavi
                }
            });
            navbar.classList.add('navbar-scrolled');
            brand.classList.add('scrolled');
            homeButtons.forEach(button => button.classList.add('scrolled'));
            logos.forEach(logo => {
                logo.src = '{{ROOT}}/CrmProject/Navbar/logo-beyaz.png';
            });
            houseIcons.forEach(icon => icon.classList.add('scrolled'));
            logoText.forEach(text => text.classList.add('scrolled'));
        } else {
            topHeader.classList.remove('scrolled');
            document.querySelector('.info-text').classList.remove('scrolled')
            links.forEach(link => {
                if (link.classList.contains('youtube')) {
                    link.style.color = ''; // Varsayılan renk
                } else if (link.classList.contains('instagram')) {
                    link.style.color = ''; // Varsayılan renk
                } else if (link.classList.contains('linkedin')) {
                    link.style.color = ''; // Varsayılan renk
                }
            });
            navbar.classList.remove('navbar-scrolled');
            brand.classList.remove('scrolled');
            homeButtons.forEach(button => button.classList.remove('scrolled'));
            logos.forEach(logo => {
                logo.src = '{{ROOT}}/CrmProject/Navbar/logo_ttw.png';
            });
            houseIcons.forEach(icon => icon.classList.remove('scrolled'));
            logoText.forEach(text => text.classList.remove('scrolled'));
        }
    });


    document.querySelectorAll('[data-bs-toggle="offcanvas"]').forEach((element) => {
        element.addEventListener('click', function () {
            const offcanvasId = element.getAttribute('data-bs-target');
            const offcanvasElement = document.querySelector(offcanvasId);
            offcanvasElement.classList.toggle('show');
        });
    });

    document.querySelectorAll('[data-bs-dismiss="offcanvas"]').forEach((element) => {
        element.addEventListener('click', function () {
            const offcanvasElement = element.closest('.offcanvas-custom');
            offcanvasElement.classList.remove('show');
        });
    });

    document.querySelectorAll('.header-link').forEach((element) => {
        element.addEventListener('click', function (e) {
            e.preventDefault();
            const selectedSection = element.getAttribute('data-content');
            if (selectedSection) {
                localStorage.setItem('lastSelectedSection', selectedSection);
                setActiveSection(selectedSection);
            } else {
                const linkId = element.id;
                if (linkId === 'homeLink') {
                    window.location.href = '#';
                }
            }
        });
    });

    function setActiveSection(sectionId) {
        document.querySelectorAll('.header-link').forEach((link) => {
            if (!link.parentElement.classList.contains('home-icon-container')) {
                link.parentElement.style.backgroundColor = '';
            }
        });
        const activeLink = document.querySelector(`.header-link[data-content="${sectionId}"]`);
        if (activeLink && !activeLink.parentElement.classList.contains('home-icon-container')) {
            activeLink.parentElement.style.backgroundColor = '#4898C0';
        }

        document.querySelectorAll('.content-section').forEach((section) => {
            section.classList.add('d-none');
        });
        const activeSection = document.getElementById(sectionId);
        if (activeSection) {
            activeSection.classList.remove('d-none');
        }
    }


    async function createNoticeCard(notice) {
        const noticeCardContainer = document.createElement('div');
        noticeCardContainer.classList.add('col-lg-3', 'col-md-6', 'mb-4', 'event-card-container');

        const noticeCard = document.createElement('div');
        noticeCard.classList.add('event-card');

        const img = document.createElement('img');
        img.src = notice.imageUrl;
        img.classList.add('img-fluid', 'rounded-start');
        img.alt = notice.NoticeName;

        const imgLink = document.createElement('a');
        imgLink.href = notice.NoticeTopic;
        imgLink.appendChild(img);

        // Duyuru başlığı için div oluştur
        const titleDiv = document.createElement('div');
        titleDiv.classList.add('card-title');
        titleDiv.textContent = notice.NoticeName;

        // Tarih ve yorum bilgisi için div oluştur
        const dateDiv = document.createElement('div');
        dateDiv.classList.add('card-text');
        dateDiv.textContent = "Tarih: " + new Date(notice.Date).toLocaleDateString('tr-TR');

        // Duyuruya git butonu
        const link = document.createElement('a');
        link.href = notice.NoticeTopic;
        link.classList.add('btn', 'btn-primary', 'btn-sm');
        link.textContent = 'Duyuruya Git';

        // Kart içeriklerini noticeCard'a ekle
        noticeCard.appendChild(imgLink);
        noticeCard.appendChild(titleDiv);
        noticeCard.appendChild(dateDiv);
        noticeCard.appendChild(link);

        // Ana container'a kartı ekle
        noticeCardContainer.appendChild(noticeCard);

        // DOM'a kartı ekle
        const announcementsRow = document.getElementById('announcementsRow');
        const allEducationCard = document.getElementById('announcementsButton');
        announcementsRow.insertBefore(noticeCardContainer, allEducationCard);
    }


    async function createBlogCard(blog) {
        const blogDiv = document.createElement('div');
        blogDiv.classList.add('col-lg-4', 'col-md-6', 'col-sm-12', 'mb-4', 'blog-item');
        
        const blogCard = document.createElement('div');
        blogCard.classList.add('card', 'h-100');
        
        const img = document.createElement('img');
        img.src = blog.imageUrl;
        img.classList.add('card-img-top');
        img.alt = blog.BlogName;

        const cardBody = document.createElement('div');
        cardBody.classList.add('card-body');
        
        const title = document.createElement('h5');
        title.classList.add('card-title', 'text-white');
        
        // Blog ismini URL dostu hale getirmek için fonksiyonu kullan
        const formattedBlogName = formatName(blog.BlogName);
        
        const titleLink = document.createElement('a');
        titleLink.href = `{{ROOT}}/blog/${formattedBlogName}`;
        titleLink.classList.add('text-white', 'text-decoration-none');
        titleLink.textContent = capitalizeWords(blog.BlogName);
        title.appendChild(titleLink);
        
        titleLink.addEventListener('click', function() {
            event.preventDefault(); // Varsayılan davranışı durdur
            const fullHref = `${titleLink.href}?id=${blog._id}`;
            window.location.href = fullHref; // Güncellenmiş href ile yönlendirme
        });
        

        
        const topic = document.createElement('p');
        topic.classList.add('card-text', 'text-white');
        topic.textContent = `${blog.WriterName} | ${blog.date} | ${category.Name}`;

        const desc = document.createElement('p');
        desc.classList.add('card-preview', 'text-white');
        desc.textContent = truncateHtmlContent(blog.Content, 50);
        
        // Append elements to card body
        cardBody.appendChild(title);
        cardBody.appendChild(topic);
        cardBody.appendChild(desc);

        // Append image and body to the card
        blogCard.appendChild(img);
        blogCard.appendChild(cardBody);

        // Append card to the main blog div
        blogDiv.appendChild(blogCard);
        
        // Append the blog card to the row in the DOM
        const announcementsRow = document.getElementById('blogRow');
        const allEducationCard = document.getElementById('blogButton');
        announcementsRow.insertBefore(blogDiv, allEducationCard);
    }

    function truncateHtmlContent(htmlString, maxLength) {
        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = htmlString;
        
        let plainText = tempDiv.textContent || tempDiv.innerText || "";

        if (plainText.length > maxLength) {
            plainText = plainText.substring(0, maxLength) + '...';
        }
        
        return plainText;
    }

    function capitalizeWords(str) {
        // Veriyi küçük harfe çevirir ve sonra her kelimenin baş harfini büyük yapar
        return str
            .toLowerCase('tr-TR')  // Türkçe karakterler için küçük harfe çevirme
            .replace(/(^|\s)\S/g, function(char) {
                return char.toUpperCase('tr-TR');  // Türkçe karakterler için baş harfi büyük yapma
            });
    }

    function formatName(courseName) {
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

});

$('#preApplicationForm').submit(async function(e) {
    e.preventDefault();
        const CourseName = $('#educationForm option:selected').text();
        const Name = $('#nameInput').val()
        const Phone = $('#phoneForm').val()
            
        fetch('https://api.talktoweb.com/PhpBack/mailSend.php',{
            method:'POST',
            headers:{'Content-Type':'application/json'},
            body: JSON.stringify({type:"ön başvuru",name:Name,phone:Phone,courseName:CourseName})
        })
        $('#preApplicationForm').trigger('reset')
});

$('#contactForm').submit(async function(e) {
    e.preventDefault();
        const CourseName = $('title').text();
        const Name = $('#nameInput').val();
        const Phone = $('#phoneInput').val();
        const Message = $('#messageInput').val()
            
        fetch('https://api.talktoweb.com/PhpBack/mailSend.php',{
            method:'POST',
            headers:{'Content-Type':'application/json'},
            body: JSON.stringify({type:"eğitmen mesaj",name:Name,phone:Phone,courseName:CourseName,message:Message})
        })
        $('#contactForm').trigger('reset')
});

$('#mainPage-form-2').submit(async function(e) {
    e.preventDefault();
        const CourseName = $('title').text();
        const Name = $('#nameSurname2').val()
        const Phone = $('#telephone2').val()
            
        fetch('https://api.talktoweb.com/PhpBack/mailSend.php',{
            method:'POST',
            headers:{'Content-Type':'application/json'},
            body: JSON.stringify({type:"size ulaşalım",name:Name,phone:Phone,courseName:CourseName})
        })
        $('#mainPage-form-2').trigger('reset')
});

$('#navbar-contact-form').submit(async function(e) {
    e.preventDefault();
        const Name = $('#fullName').val()
        const Phone = $('#phone').val()
        const Email = $('#email').val()
        const Konu = $('#subject').val()
        const Message = $('#message').val()
            
        fetch('https://api.talktoweb.com/PhpBack/mailSend.php',{
            method:'POST',
            headers:{'Content-Type':'application/json'},
            body: JSON.stringify({type:"size ulaşalım",name:Name,phone:Phone,email:Email,konu:Konu,message:Message})
        })
        $('#navbar-contact-form').trigger('reset')
});



const endTime = Date.now();
const elapsedTime = (endTime - startTime) / 1000;
console.log(`Toplam süre: ${elapsedTime.toFixed(2)} saniye`);

function detectIdType(id) {
    if (/^[0-9a-fA-F]{24}$/.test(id)) {
        return id.toString() ;
    } else if (!isNaN(id) && Number.isInteger(parseFloat(id))) {
        return parseInt(id);
    }
    return null; // Geçersiz ID
}
