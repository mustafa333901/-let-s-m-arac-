from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "zeldo_secret_key"

# 1. Giriş ve Kayıt Sayfası
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def handle_login():
    email = request.form['email']
    password = request.form['password']
    # Giriş kontrolü (örnek doğrulama)
    if email == "test@zeldo.com" and password == "password":
        session['user'] = email
        return redirect(url_for('home'))
    return "Hatalı giriş, tekrar deneyin!"

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def handle_register():
    # Yeni kullanıcı kaydı işlemi
    return redirect(url_for('login'))

# 2. Ana Sayfa (Kişiselleştirilmiş Akış)
@app.route('/home')
def home():
    if 'user' in session:
        feed = [
            {"content": "Yeni gönderi 1", "author": "Kullanıcı A"},
            {"content": "Yeni gönderi 2", "author": "Kullanıcı B"}
        ]
        return render_template('home.html', user=session['user'], feed=feed)
    return redirect(url_for('login'))

# 3. Profil Sayfası
@app.route('/profile')
def profile():
    if 'user' in session:
        user_data = {
            "name": "Test Kullanıcı",
            "bio": "Merhaba, bu benim biyografim.",
            "posts": ["Gönderim 1", "Gönderim 2"],
            "followers": 15,
            "following": 10
        }
        return render_template('profile.html', user=user_data)
    return redirect(url_for('login'))

# 4. Grup Sayfası (Yeni Özellikler: Grup Yönetimi)
@app.route('/group/<int:group_id>')
def group(group_id):
    group_data = {
        "id": group_id,
        "name": f"Grup {group_id}",
        "members": ["Kullanıcı 1", "Kullanıcı 2"],
        "admin": "Kullanıcı 1"
    }
    return render_template('group.html', group=group_data)

@app.route('/group/create', methods=['GET', 'POST'])
def create_group():
    if request.method == 'POST':
        # Grup oluşturma işlemi
        return redirect(url_for('home'))
    return render_template('create_group.html')

# 5. Keşfet Sayfası (Kategori Filtreleme ve Arama)
@app.route('/explore')
def explore():
    categories = ["Sanat", "Teknoloji", "Eğitim", "Eğlence"]
    trending = [{"title": "Popüler İçerik 1"}, {"title": "Popüler İçerik 2"}]
    return render_template('explore.html', categories=categories, trending=trending)

@app.route('/explore/search', methods=['POST'])
def explore_search():
    query = request.form['query']
    # Arama işlemi (örnek)
    results = [{"title": f"Arama sonucu: {query}"}]
    return render_template('search_results.html', results=results)

# 6. Mesajlaşma Sayfası (Yeni Özellik: Grup Sohbeti)
@app.route('/messages')
def messages():
    if 'user' in session:
        chat_history = [
            {"sender": "Kullanıcı 1", "message": "Merhaba!"},
            {"sender": "Sen", "message": "Nasılsın?"}
        ]
        return render_template('messages.html', messages=chat_history)
    return redirect(url_for('login'))

@app.route('/messages/group/<int:group_id>')
def group_messages(group_id):
    group_chat = [{"sender": "Üye 1", "message": "Merhaba Grup!"}]
    return render_template('group_messages.html', group_chat=group_chat)

# 7. Bildirimler (Etkinlik Bildirimleri)
@app.route('/notifications')
def notifications():
    if 'user' in session:
        notifications = [
            "Grup X'e yeni üye katıldı.",
            "Gönderiniz beğenildi.",
            "Yeni etkinlik: Teknoloji Zirvesi"
        ]
        return render_template('notifications.html', notifications=notifications)
    return redirect(url_for('login'))

# 8. Ayarlar (Tema Değiştirme ve Dil Seçenekleri)
@app.route('/settings')
def settings():
    if 'user' in session:
        themes = ["Karanlık", "Aydınlık"]
        languages = ["Türkçe", "İngilizce"]
        return render_template('settings.html', themes=themes, languages=languages)
    return redirect(url_for('login'))

@app.route('/settings/update', methods=['POST'])
def update_settings():
    # Ayarları güncelleme işlemi
    return redirect(url_for('settings'))

# 9. Oyunlaştırma ve Ödüller (Başarımlar ve Seviyeler)
@app.route('/rewards')
def rewards():
    if 'user' in session:
        achievements = [
            {"name": "Görev 1", "status": "Tamamlandı!"},
            {"name": "Görev 2", "status": "Devam Ediyor"}
        ]
        level = {"current": 5, "next": 6, "progress": 75}
        return render_template('rewards.html', achievements=achievements, level=level)
    return redirect(url_for('login'))

# 10. Yardım ve Destek (Canlı Destek ve SSS)
@app.route('/help')
def help():
    faqs = [
        {"question": "Nasıl kayıt olurum?", "answer": "Giriş sayfasından 'Kayıt Ol' seçeneğini tıklayın."},
        {"question": "Şifremi unuttum, ne yapmalıyım?", "answer": "Giriş sayfasındaki 'Şifremi Unuttum' seçeneğini kullanın."}
    ]
    return render_template('help.html', faqs=faqs)

@app.route('/help/live')
def live_support():
    # Canlı destek bağlantısı
    return "Canlı destek şu an aktif değil."

# 11. Çıkış
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
