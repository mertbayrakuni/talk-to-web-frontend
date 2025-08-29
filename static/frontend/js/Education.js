document.addEventListener('DOMContentLoaded', function () {
    const mainImage = document.getElementById('mainImage');
    const previewImages = Array.from(document.querySelectorAll('.preview-img'));
    var originalMainSrc;
    const originalPreviewSrcs = previewImages.map(img => img.src);
    const tabLinks = document.querySelectorAll('.nav-link');
    const images = [];
    const wp = document.getElementById('whatsapp');
    const prevButton = document.getElementById('prevButton');
    const nextButton = document.getElementById('nextButton');
    const tabs = document.querySelector('.tab-section .nav-tabs');
    const navbar = document.getElementById('header-cont');
    let a;
    let currentIndex = 0;

    // Aktif sekme ayarlama
    function setActiveTab(tab) {
        tabLinks.forEach(link => {
            link.classList.remove('active');
            document.querySelector(link.getAttribute('href')).classList.remove('show', 'active');
            $('.nav-link').css({
                'background-color': 'rgb(248, 249, 250)',
                'color': '#000',
                'border-top': 'none'
            });
            $('.nav-link').removeClass('custom-after');
        });
        tab.classList.add('active');
        document.querySelector(tab.getAttribute('href')).classList.add('show', 'active');

        // Sticky durumdaysa, active tab görünümünü güncelle
        if (tabs.classList.contains('sticky')) {
            $('.nav-link.active').css({
                'background-color': 'rgb(0 170 255)',
                'color': '#ffffff',
                'border-top': '1px solid white'
            });
            $('.nav-link.active').addClass('custom-after');
        }

        // Sticky noktaya geri dön
        const stickyPoint = a;
        if (window.scrollY > stickyPoint) {
            window.scrollTo({ top: stickyPoint, behavior: 'smooth' });
        }
    }

    setActiveTab(tabLinks[0]);

    tabLinks.forEach(tab => {
        tab.addEventListener('click', function (e) {
            e.preventDefault();
            localStorage.setItem('selectedTab', tab.getAttribute('href'));
            setActiveTab(tab);
        });
    });

    function adjustTabsPosition() {
        const totalHeight = navbar.offsetHeight;
        tabs.style.top = `${totalHeight}px`;

        if (window.scrollY >= tabs.offsetTop - totalHeight) {
            tabs.classList.add('sticky');
            tabs.style.zIndex = "1018";

            $('.navbar-custom').css('box-shadow', 'none');
            $('.nav-link').css('background-color', 'transparent');
            $('.nav-link').addClass('no-border-radius');

            $('.nav-link.active').css({
                'background-color': 'rgb(0 170 255)',
                'color': '#ffffff',
                'border-top': '1px solid white'
            });
            $('.nav-link.active').addClass('custom-after');

        } else {
            tabs.classList.remove('sticky');
            tabs.style.padding = "0";

            $('.navbar-custom').css('box-shadow', '0 8px 16px rgba(0, 0, 0, 0.3)');
            $('.nav-link').css({
                'background-color': 'rgb(248, 249, 250)',
                'color': '#000',
                'border-top': 'none'
            });
            $('.nav-link').removeClass('custom-after');
        }
    }

    function updateImage(index) {
        mainImage.src = images[index];
    }

    prevButton.addEventListener('click', () => {
        currentIndex = (currentIndex === 0) ? images.length - 1 : currentIndex - 1;
        updateImage(currentIndex);
    });

    nextButton.addEventListener('click', () => {
        currentIndex = (currentIndex === images.length - 1) ? 0 : currentIndex + 1;
        updateImage(currentIndex);
    });

    const kayitOlCard = document.querySelector('.kayit-ol-card');

    function checkVisibility() {
        const triggerElement = document.getElementById('triggerCheck');
        if (!triggerElement) return;

        const triggerPosition = triggerElement.getBoundingClientRect().bottom;
        if (triggerPosition <= 0) {
            kayitOlCard.classList.remove('d-none');
            if(window.innerWidth <= 768){
                wp.style.bottom = "170px";
            }
        } else {
            wp.style.bottom = "";
            kayitOlCard.classList.add('d-none');
        }
    }

    window.addEventListener('scroll', checkVisibility);
    window.addEventListener('resize', checkVisibility);
    window.addEventListener('resize', adjustTabsPosition);
    window.addEventListener('scroll', adjustTabsPosition);

    // Kurs detaylarını doldur
    function froalaEdit(element) {
        var tempDiv = document.createElement('div');
        tempDiv.innerHTML = element;

        // Stil özniteliğine sahip tüm elementleri bul ve stil özniteliklerini temizle
        const elementsWithStyle = tempDiv.querySelectorAll('[style]:not(img):not(video)');
        elementsWithStyle.forEach(el => {
            let style = el.getAttribute('style');
            style = style.replace(/width\s*[^;]+;?/gi, '');
            el.setAttribute('style', style);
        });

        // `data-f-id="pbf"` özniteliğine sahip tüm `<p>` etiketlerini sil
        const paragraphsToRemove = tempDiv.querySelectorAll('p[data-f-id="pbf"]');
        paragraphsToRemove.forEach(p => {
            p.remove(); // `<p>` etiketini tamamen kaldır
        });

        return tempDiv.innerHTML;
    }

    async function populateCourseDetails(groupId) {
    try {
        const [response, instructorResponse] = await Promise.all([
            sendApiRequest('groups'),
            sendApiRequest('iUsers')
        ]);

        const group = response.find(item => item._id === detectIdType(groupId));
        if (!group) return;

        mainImage.src = group.Course.Img || 'https://via.placeholder.com/600x800';
        originalMainSrc = group.Course.Img;
        images.push(originalMainSrc);
        document.querySelectorAll('.course-title').forEach(element => {
            element.textContent = group.Course.CourseName || 'Kurs Başlığı';
        });
        document.querySelector('.card-text.info').innerHTML = froalaEdit(group.Description) || 'Açıklama Bulunamadı';
        
        // Clear previous instructor information
        const instructorInfoContainer = document.querySelector('.instructor-info .row');
        instructorInfoContainer.innerHTML = '';

        // Loop through Instructor array
        for (const instructorId of group.Instructor) {
            const iud = instructorResponse.find(item => item._id === detectIdType(instructorId));
            if (iud) {
                // Create new instructor column
                const instructorCol = document.createElement('div');
                instructorCol.classList.add('col');

                // Set instructor image, name, and LinkedIn link
                const img = document.createElement('img');
                img.classList.add('instructor-img');
                img.src = iud.User?.img || 'https://via.placeholder.com/150';

                const nameP = document.createElement('p');
                const nameCard = document.querySelector('.kayit-ol-card .card-instructor')
                nameP.classList.add('instructor-name', 'mb-1');
                nameP.textContent = iud.User?.fullName || 'Eğitmen Bilgisi Yok';
                nameCard.textContent += iud.User?.fullName || 'Eğitmen Bilgisi Yok';

                const linkP = document.createElement('p');
                linkP.classList.add('instructor-link');
                const linkA = document.createElement('a');
                linkA.href = iud.User?.LinkedIn || '#';
                linkA.target = '_blank';
                linkA.innerHTML = '<i class="bi bi-linkedin"></i>';
                linkP.appendChild(linkA);

                // Append elements to instructor column
                instructorCol.appendChild(img);
                instructorCol.appendChild(nameP);
                instructorCol.appendChild(linkP);

                // Append instructor column to the row
                instructorInfoContainer.appendChild(instructorCol);
            }
        }

        // Continue with other elements
        document.querySelector('.kayit-ol-card .card-title').textContent = group.Course.CourseName || 'Bilgi Alınamadı';
        document.querySelector('.kayit-ol-card .card-date').textContent = `${new Date(group.StartDate).toLocaleDateString()} - ${new Date(group.FinishDate).toLocaleDateString()}` || 'Bilgi Alınamadı';
        document.querySelector('.kayit-ol-card .card-image img').src = group.MainImg || 'https://via.placeholder.com/600x800';

        // Update preview images, tabs, and visibility checks
        updatePreviewImages(group);
        updateTabsContent(group);
        updateOpenContent(group);
        
        updateMetaTags(`${group.Course.CourseName} | Talk to Web`,group.Course.MetaDesc)

    } catch (error) {
        console.error('Error populating course details:', error);
    } finally {
        a = tabs.offsetTop - navbar.offsetHeight;
        const endTime = Date.now();
        const elapsedTime = (endTime - startTime) / 1000;
        console.log(`Toplam süre: ${elapsedTime.toFixed(2)} saniye`);
    }
}

function updatePreviewImages(group) {
    if (group.SideImg && group.SideImg.length) {
        images.push(...group.SideImg);

        previewImages.forEach((img, index) => {
            if (group.SideImg[index]) {
                img.src = group.SideImg[index];
                img.parentElement.style.display = 'block';
            } else {
                img.parentElement.style.display = 'none';
            }
        });

        prevButton.style.display = images.length > 1 ? 'block' : 'none';
        nextButton.style.display = images.length > 1 ? 'block' : 'none';
    } else {
        previewImages.forEach(img => img.parentElement.style.display = 'none');
        prevButton.classList.add('d-none');
        nextButton.classList.add('d-none');
    }
}

function updateTabsContent(group) {
    document.getElementById('tab-overview').innerHTML = group.Content ? froalaEdit(group.Content) : 'İçerik verileri bulunamadı.';
    document.getElementById('tab-curriculum').innerHTML = group.Curriculum ? froalaEdit(group.Curriculum) : 'Müfredat verileri bulunamadı.';
    document.getElementById('tab-faq').innerHTML = group.SSS ? froalaEdit(group.SSS) : 'Bu kurs ile ilgili sıkça sorulan sorular bulunmamaktadır.';
    document.getElementById('tab-seo').innerHTML = group.SEO ? froalaEdit(group.SEO) : document.getElementById('tab-seo').classList.add('d-none');
}

function updateOpenContent(group) {
    const openContent = document.getElementById('dynamic-content');
    openContent.innerHTML = group.Open
        ? `<div class="mt-2"><button class="btn btn-primary btn-lg mb-3" id="triggerCheck" aria-label="Kayıt Ol">Kayıt Ol</button></div>`
        : `<form id="bilgilendirme"><textarea id="infoReq" class="form-control mb-3" rows="5" style="resize: none;" placeholder="Bu eğitimin süresi geçti. Bir sonraki eğitimden haberdar olmak istiyorsanız; bu alana adınızı-soyadınızı, e-posta adresinizi, varsa notunuzu ekleyip bilgi talebinde bulunabilirsiniz"></textarea><button type="submit" class="btn btn-primary">Gönder</button></form>`;
    if($('#triggerCheck')){
        $('#triggerCheck').on('click', function () {
            $('#registrationModal').modal('show');
        });
   
    }
    
    $('#bilgilendirme').on('submit', async function (e) {
        e.preventDefault();
        const CourseName = group.Course.CourseName;
        const Name = $('#infoReq').val();

        fetch('https://api.talktoweb.com/PhpBack/mailSend.php', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                type: "ders bilgi",
                name: Name,
                courseName: CourseName
            })
        });
        $('#bilgilendirme').trigger('reset');
    });
}

    const urlParams = new URLSearchParams(window.location.search);
    const groupId = urlParams.get('id');
    if (groupId) populateCourseDetails(groupId);
});

$(document).ready(function () {
    $('#modal-button-2').on('click', function () {
        $('#registrationModal').modal('show');
    });
    
    $('#registrationForm').on('submit', async function (e) {
        e.preventDefault();
        const CourseName = group.Course.CourseName;
        const Name = $('#nameSurname').val();
        const Phone = $('#phoneKayit').val();

        await fetch('https://api.talktoweb.com/PhpBack/mailSend.php', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                type: "ders kayıt",
                name: Name,
                phone: Phone,
                courseName: CourseName
            })
        });

        $('#registrationForm').trigger('reset');
        $('#registrationModal').modal('hide');
    });
});

function updateMetaTags(title, description) {
    document.title = title;

    const metaDescription = document.querySelector('meta[name="description"]');
    if (metaDescription) {
        metaDescription.setAttribute("content", description);
    } else {
        const newMetaDescription = document.createElement('meta');
        newMetaDescription.name = "description";
        newMetaDescription.content = description;
        document.head.appendChild(newMetaDescription);
    }

    const ogTitle = document.querySelector('meta[property="og:title"]');
    if (ogTitle) {
        ogTitle.setAttribute("content", title);
    }

    const ogDescription = document.querySelector('meta[property="og:description"]');
    if (ogDescription) {
        ogDescription.setAttribute("content", description);
    }
}

// Örnek kullanım
updateMetaTags("Yeni Başlık", "Bu sayfa hakkında dinamik açıklama.");