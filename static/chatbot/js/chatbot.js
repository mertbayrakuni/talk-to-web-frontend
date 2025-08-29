/* global window, document, location */

window.TTWChatbot = (function () {
    // --- tiny DOM helper (linter-friendly defaults) ---
    function h(tag, attrs /* optional */, kids /* rest via arguments */) {
        var el = document.createElement(tag);
        var a = attrs || {};
        Object.keys(a).forEach(function (k) {
            var v = a[k];
            if (k === 'class') el.className = v;
            else if (k.indexOf('on') === 0 && typeof v === 'function') el.addEventListener(k.slice(2), v);
            else el.setAttribute(k, v);
        });
        for (var i = 2; i < arguments.length; i += 1) {
            el.append(arguments[i]);
        }
        return el;
    }

    function addMsg(chatEl, text, who) {
        var klass = 'ttw-msg ' + (who === 'user' ? 'is-user' : 'is-bot');
        var wrap = h('div', {'class': klass}, text);
        wrap.append(h('div', {'class': 'ttw-timestamp'}, new Date().toTimeString().slice(0, 5)));
        chatEl.append(wrap);
        chatEl.scrollTop = chatEl.scrollHeight;
    }

    function computeEndpoint(root, opts) {
        var scheme = location.protocol === 'https:' ? 'wss' : 'ws';

        // 1) explicit option
        if (opts.endpoint) return opts.endpoint;

        // 2) data-endpoint attr on the root
        var attrEp = root && root.getAttribute('data-endpoint');
        if (attrEp) return attrEp;

        // 3) explicit wsPort on same hostname
        if (opts.wsPort) {
            var host = location.hostname + ':' + String(opts.wsPort);
            return scheme + '://' + host + '/ws';
        }

        // 4) common dev split: page on :9000, WS on :8000
        if (location.port === '9000') {
            return scheme + '://' + location.hostname + ':8000/ws';
        }

        // 5) default: same host (works with single ngrok tunnel that proxies /ws)
        return scheme + '://' + location.host + '/ws';
    }

    function mount(host, opts) {
        opts = opts || {};

        // 1) ensure a root exists (supports pre-rendered partial OR JS-built)
        var root = host.querySelector('[data-ttw-chatbot]');
        if (!root) {
            root = h('div', {'class': 'ttw-chatbot', 'data-ttw-chatbot': ''},
                h('header', {'class': 'ttw-header'},
                    h('h2', {}, 'AI Chatbot'),
                    h('div', {'class': 'subtitle'}, 'Size yardımcı olmak için buradayım')
                ),
                h('div', {'class': 'ttw-chat', role: 'log', 'aria-live': 'polite'}),
                h('form', {'class': 'ttw-input'},
                    h('input', {'class': 'ttw-input-field', type: 'text', placeholder: 'Mesajınızı yazın...'}),
                    // IMPORTANT: type="button" so clicks never submit the page
                    h('button', {'class': 'ttw-send', type: 'button'}, 'Gönder')
                )
            );
            host.append(root);
        }

        // prefer new classes; fall back to legacy IDs if present
        var chat = root.querySelector('.ttw-chat') || root.querySelector('#chat');
        var input = root.querySelector('.ttw-input-field') || root.querySelector('#msgInput');
        var form = root.querySelector('.ttw-input') || root.querySelector('#ttw-form');
        var sendBtn = root.querySelector('.ttw-send');

        // 2) bind button click (most reliable)
        if (sendBtn) {
            sendBtn.addEventListener('click', function (ev) {
                ev.preventDefault();
                ev.stopPropagation();
                send();
            });
        }

        // 3) also guard the form submit (in case markup still has type="submit")
        if (form) {
            form.addEventListener('submit', function (ev) {
                ev.preventDefault();
                ev.stopPropagation();
                send();
            });
        }

        // 4) websocket with robust reconnect + queue
        var endpoint = computeEndpoint(root, opts);
        var ws = null;
        var isOpen = false;
        var pending = [];
        var initialSent = false;

        function connect() {
            try {
                ws = new WebSocket(endpoint);
                ws.addEventListener('open', onOpen);
                ws.addEventListener('message', onMessage);
                ws.addEventListener('close', onClose);
                ws.addEventListener('error', onError);
            } catch (e) {
                onClose();
            }
        }

        function onOpen() {
            isOpen = true;

            // flush queue
            while (pending.length) {
                try {
                    ws.send(pending.shift());
                } catch (e) {
                }
            }

            // one-time initial message (from mini form)
            if (opts.initialText && !initialSent && input) {
                input.value = opts.initialText;
                send();
                initialSent = true;
            }
        }

        function onError() {
            // let onClose handle backoff
        }

        function onClose() {
            isOpen = false;
            setTimeout(connect, 800);
        }

        function sendRaw(s) {
            if (!s) return;
            if (ws && ws.readyState === 1 && isOpen) {
                try {
                    ws.send(s);
                } catch (e) {
                }
            } else {
                pending.push(s);
            }
        }

        function send() {
            var text = (input && input.value ? input.value : '').trim();
            if (!text) return;
            addMsg(chat, text, 'user');
            sendRaw(text);
            if (input) input.value = '';
        }

        function onMessage(e) {
            try {
                var data = JSON.parse(e.data);
                if (data.reply) addMsg(chat, data.reply, 'bot');

                if (data.urls && data.urls.length) {
                    var imgs = h('div', {'class': 'ttw-images'});
                    data.urls.forEach(function (u) {
                        var img = h('img', {src: u.image, title: u.adres});
                        img.onclick = function () {
                            addMsg(chat, 'Seçilen adres: ' + u.adres, 'user');
                            sendRaw(u.adres);
                        };
                        imgs.append(img);
                    });
                    chat.append(imgs);
                    chat.scrollTop = chat.scrollHeight;
                }
            } catch (e) {
            }
        }

        connect(); // start

        function destroy() {
            try {
                if (ws) ws.close();
            } catch (e) {
            }
            host.innerHTML = '';
        }

        return {destroy: destroy};
    }

    return {mount: mount};
})();
