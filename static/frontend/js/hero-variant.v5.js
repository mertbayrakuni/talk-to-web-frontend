(function () {
    // surface unexpected runtime errors
    window.addEventListener("error", function (e) {
        console.error("[HERO] window error:", e.message);
    });

    console.log("[HERO] File loaded");

    // 5 variants (edit freely)
    const VARIANTS = [
        {id: "a", img: "/static/frontend/img/hero-1.webp", title: "Kariyerini Bugün Tasarla"},
        {id: "b", img: "/static/frontend/img/hero-2.webp", title: "Tech ile Geleceğini Kur"},
        {id: "c", img: "/static/frontend/img/hero-3.webp", title: "Hayalindeki İşe Yaklaş"},
        {id: "d", img: "/static/frontend/img/hero-4.webp", title: "Yeni Beceriler, Yeni Sen"},
        {id: "e", img: "/static/frontend/img/hero-5.webp", title: "Öğren, Geliş, Parla"}
    ];

    // session-scoped helpers (per tab/window)
    function getVariant() {
        try {
            return sessionStorage.getItem("ttw_hero_variant");
        } catch {
            return null;
        }
    }

    function setVariant(id) {
        try {
            sessionStorage.setItem("ttw_hero_variant", id);
        } catch {
        }
    }

    function chooseVariantId() {
        const i = Math.floor(Math.random() * VARIANTS.length);
        console.log("[HERO] Random index", i, "->", VARIANTS[i].id);
        return VARIANTS[i].id;
    }

    function applyVariant(v) {
        const hero = document.querySelector(".bg-header");
        const h1 = document.querySelector(".kariyer-header");

        if (hero) {
            hero.style.setProperty("--hero-url", `url('${v.img}')`);
            console.log("[HERO] Applied background:", v.img);
        } else {
            console.warn("[HERO] .bg-header not found");
        }

        if (h1) {
            h1.innerHTML = v.title;
            console.log("[HERO] Updated title:", v.title);
        } else {
            console.warn("[HERO] .kariyer-header not found");
        }
    }

    function init() {
        console.log("[HERO] Init…");

        let id = getVariant();
        if (!id) {
            id = chooseVariantId();
            setVariant(id);
            console.log("[HERO] New session pick:", id);
        } else {
            console.log("[HERO] Using session pick:", id);
        }

        const v = VARIANTS.find(x => x.id === id) || VARIANTS[0];

        // Preload, then apply
        const img = new Image();
        img.onload = function () {
            console.log("[HERO] Preload success");
            applyVariant(v);
        };
        img.onerror = function () {
            console.warn("[HERO] Preload failed; applying anyway");
            applyVariant(v);
        };
        img.src = v.img;
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", init);
    } else {
        init();
    }
})();
