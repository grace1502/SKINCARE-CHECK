<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🧪 Pemeriksa Keamanan Skincare</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(rgba(248, 187, 217, 0.85), rgba(221, 160, 221, 0.85)), 
                        url('https://images.unsplash.com/photo-1596462502278-27bfdc403348?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2940&q=80');
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            background-repeat: no-repeat;
            min-height: 100vh;
            line-height: 1.6;
            color: #333;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        /* Header */
        .header {
            background: linear-gradient(135deg, #FF69B4 0%, #FFB6C1 100%);
            padding: 2rem;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 8px 32px rgba(255, 105, 180, 0.3);
            margin-bottom: 2rem;
            backdrop-filter: blur(10px);
        }

        .header h1 {
            color: white;
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }

        .header p {
            color: rgba(255,255,255,0.9);
            font-size: 1.2rem;
        }

        /* Navigation */
        .nav {
            background: rgba(255, 255, 255, 0.25);
            backdrop-filter: blur(20px);
            border-radius: 15px;
            padding: 1rem;
            margin-bottom: 2rem;
            box-shadow: 0 4px 15px rgba(255, 182, 193, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .nav ul {
            list-style: none;
            display: flex;
            justify-content: center;
            gap: 2rem;
        }

        .nav-item {
            padding: 0.8rem 1.5rem;
            background: linear-gradient(135deg, #FFB6C1 0%, #FFC0CB 100%);
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            color: #8b1538;
            font-weight: bold;
            box-shadow: 0 2px 10px rgba(255, 192, 203, 0.4);
        }

        .nav-item:hover, .nav-item.active {
            background: linear-gradient(135deg, #FF69B4 0%, #FFB6C1 100%);
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(255, 105, 180, 0.5);
        }

        /* Content Sections */
        .content-section {
            display: none;
            background: rgba(255, 255, 255, 0.25);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 8px 32px rgba(255, 182, 193, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .content-section.active {
            display: block;
            animation: fadeIn 0.5s ease-in;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Home Section */
        .hero {
            text-align: center;
            padding: 3rem 0;
        }

        .hero h2 {
            color: #8b1538;
            font-size: 2.2rem;
            margin-bottom: 1rem;
        }

        .hero p {
            font-size: 1.1rem;
            color: #5a1a2e;
            margin-bottom: 2rem;
        }

        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }

        .feature-card {
            background: linear-gradient(135deg, #FFC0CB 0%, #FFE4E1 100%);
            padding: 2rem;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(255, 192, 203, 0.3);
            transition: transform 0.3s ease;
        }

        .feature-card:hover {
            transform: translateY(-5px);
        }

        .feature-card h3 {
            color: #8b1538;
            margin-bottom: 1rem;
            font-size: 1.3rem;
        }

        /* Analyzer Section */
        .analyzer-form {
            background: rgba(255, 255, 255, 0.3);
            backdrop-filter: blur(15px);
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 4px 15px rgba(255, 182, 193, 0.2);
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        .form-group label {
            display: block;
            color: #8b1538;
            font-weight: bold;
            margin-bottom: 0.5rem;
            font-size: 1.1rem;
        }

        .form-group textarea {
            width: 100%;
            padding: 1rem;
            border: 2px solid #DDA0DD;
            border-radius: 10px;
            font-size: 16px;
            background: rgba(255, 255, 255, 0.9);
            color: #333;
            resize: vertical;
            min-height: 120px;
        }

        .form-group textarea::placeholder {
            color: #999;
        }

        .analyze-btn {
            background: linear-gradient(135deg, #FF69B4 0%, #FFB6C1 100%);
            color: white;
            border: none;
            padding: 1rem 2rem;
            border-radius: 10px;
            font-size: 1.1rem;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(255, 105, 180, 0.3);
        }

        .analyze-btn:hover {
            background: linear-gradient(135deg, #FF1493 0%, #FF69B4 100%);
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(255, 105, 180, 0.4);
        }

        /* Results */
        .results {
            margin-top: 2rem;
        }

        .safe-result {
            background: linear-gradient(135deg, #90EE90 0%, #98FB98 100%);
            padding: 1.5rem;
            border-radius: 15px;
            border-left: 5px solid #28a745;
            color: #2d5016;
            box-shadow: 0 4px 15px rgba(144, 238, 144, 0.4);
        }

        .danger-result {
            background: linear-gradient(135deg, #FFB6C1 0%, #FF91A4 100%);
            padding: 1.5rem;
            border-radius: 15px;
            border-left: 5px solid #dc3545;
            color: #721c24;
            box-shadow: 0 4px 15px rgba(255, 145, 164, 0.4);
            margin-bottom: 1rem;
        }

        .ingredient-item {
            background: rgba(255, 255, 255, 0.8);
            padding: 1rem;
            border-radius: 10px;
            margin: 1rem 0;
            border-left: 4px solid #dc3545;
            box-shadow: 0 2px 10px rgba(255, 192, 203, 0.3);
        }

        .ingredient-name {
            font-weight: bold;
            color: #8b1538;
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
        }

        .risk-level {
            color: #dc3545;
            font-weight: bold;
        }

        .learn-more-btn {
            background: linear-gradient(135deg, #DDA0DD 0%, #E8D5F2 100%);
            color: #8b1538;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            cursor: pointer;
            margin-top: 0.5rem;
            font-size: 0.9rem;
            transition: all 0.3s ease;
        }

        .learn-more-btn:hover {
            background: linear-gradient(135deg, #D8BFD8 0%, #DDA0DD 100%);
            transform: scale(1.05);
        }

        .ingredient-details {
            display: none;
            margin-top: 1rem;
            padding: 1rem;
            background: rgba(255, 255, 255, 0.5);
            border-radius: 8px;
            border: 1px solid #DDA0DD;
        }

        .ingredient-details.show {
            display: block;
            animation: slideDown 0.3s ease;
        }

        @keyframes slideDown {
            from { opacity: 0; max-height: 0; }
            to { opacity: 1; max-height: 200px; }
        }

        /* About Section */
        .about-content {
            color: #5a1a2e;
            line-height: 1.8;
        }

        .about-content h3 {
            color: #8b1538;
            margin: 2rem 0 1rem 0;
        }

        .warning-box {
            background: linear-gradient(135deg, #FFE4B5 0%, #FFEAA7 100%);
            padding: 1.5rem;
            border-radius: 10px;
            border-left: 5px solid #FF8C00;
            margin: 1.5rem 0;
            color: #8B4513;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .nav ul {
                flex-direction: column;
                gap: 1rem;
            }

            .header h1 {
                font-size: 2rem;
            }

            .hero h2 {
                font-size: 1.8rem;
            }

            .container {
                padding: 10px;
            }
        }

        .loading {
            display: none;
            text-align: center;
            padding: 2rem;
            color: #8b1538;
        }

        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #FF69B4;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 1rem;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <h1>🧪 Pemeriksa Keamanan Skincare</h1>
            <p>Periksa keamanan produk skincare Anda dengan mudah dan cepat</p>
        </header>

        <nav class="nav">
            <ul>
                <li class="nav-item active" onclick="showSection('home')">🏠 Beranda</li>
                <li class="nav-item" onclick="showSection('analyzer')">🔍 Analisis</li>
                <li class="nav-item" onclick="showSection('about')">ℹ️ Tentang</li>
            </ul>
        </nav>

        <!-- Home Section -->
        <section id="home" class="content-section active">
            <div class="hero">
                <h2>Selamat Datang di Pemeriksa Keamanan Skincare</h2>
                <p>Platform terpercaya untuk menganalisis keamanan bahan-bahan dalam produk perawatan kulit Anda</p>
            </div>
            
            <div class="features">
                <div class="feature-card">
                    <h3>🔬 Analisis Mendalam</h3>
                    <p>Sistem kami memeriksa lebih dari 20 jenis bahan berbahaya yang umum ditemukan dalam produk skincare</p>
                </div>
                
                <div class="feature-card">
                    <h3>⚡ Hasil Instan</h3>
                    <p>Dapatkan hasil analisis dalam hitungan detik dengan penjelasan detail tentang setiap bahan berbahaya</p>
                </div>
                
                <div class="feature-card">
                    <h3>📚 Edukasi Komprehensif</h3>
                    <p>Pelajari mengapa bahan tertentu berbahaya dan bagaimana mereka dapat mempengaruhi kesehatan kulit Anda</p>
                </div>
                
                <div class="feature-card">
                    <h3>🛡️ Keamanan Terjamin</h3>
                    <p>Database kami didasarkan pada regulasi dan penelitian ilmiah terkini dari berbagai organisasi kesehatan</p>
                </div>
            </div>
        </section>

        <!-- Analyzer Section -->
        <section id="analyzer" class="content-section">
            <h2 style="color: #8b1538; margin-bottom: 2rem;">📝 Analisis Bahan Skincare</h2>
            
            <div class="analyzer-form">
                <div class="form-group">
                    <label for="ingredients">Masukkan Daftar Bahan Skincare:</label>
                    <textarea 
                        id="ingredients" 
                        placeholder="Contoh: Aqua, Glycerin, Alcohol, Fragrance, Sodium Laureth Sulfate, Methylparaben"
                    ></textarea>
                </div>
                
                <button class="analyze-btn" onclick="analyzeIngredients()">
                    🔍 Analisis Bahan
                </button>
            </div>

            <div class="loading" id="loading">
                <div class="spinner"></div>
                <p>Sedang menganalisis bahan-bahan...</p>
            </div>

            <div class="results" id="results"></div>
        </section>

        <!-- About Section -->
        <section id="about" class="content-section">
            <div class="about-content">
                <h2 style="color: #8b1538; margin-bottom: 2rem;">ℹ️ Tentang Aplikasi</h2>
                
                <p>Pemeriksa Keamanan Skincare adalah alat digital yang dirancang untuk membantu konsumen membuat keputusan yang lebih baik tentang produk perawatan kulit yang mereka gunakan. Aplikasi ini menganalisis daftar bahan (ingredients) pada produk skincare dan memberikan peringatan tentang bahan-bahan yang berpotensi berbahaya.</p>

                <h3>🎯 Tujuan Aplikasi</h3>
                <p>Kami berkomitmen untuk meningkatkan kesadaran konsumen tentang bahan-bahan dalam produk skincare dan membantu mereka membuat pilihan yang lebih aman untuk kesehatan kulit mereka.</p>

                <h3>🔬 Metodologi</h3>
                <p>Database kami mencakup lebih dari 20 kategori bahan berbahaya yang didasarkan pada:</p>
                <ul style="margin: 1rem 0; padding-left: 2rem;">
                    <li>Regulasi Uni Eropa (EU Regulation No. 1223/2009)</li>
                    <li>Penelitian ilmiah terpublikasi</li>
                    <li>Panduan dari organisasi kesehatan internasional</li>
                    <li>Standar keamanan kosmetik global</li>
                </ul>

                <h3>🛡️ Kategori Risiko</h3>
                <p>Setiap bahan berbahaya dikategorikan berdasarkan tingkat risikonya:</p>
                <ul style="margin: 1rem 0; padding-left: 2rem;">
                    <li><strong>Kritis:</strong> Bahan yang sangat berbahaya (contoh: mercury, lead)</li>
                    <li><strong>Tinggi:</strong> Bahan dengan potensi bahaya signifikan</li>
                    <li><strong>Sedang:</strong> Bahan yang dapat menyebabkan iritasi atau masalah ringan</li>
                </ul>

                <div class="warning-box">
                    <h4>⚠️ Penting untuk Diingat</h4>
                    <p>Aplikasi ini adalah alat bantu edukasi dan bukan pengganti konsultasi dengan profesional kesehatan. Keamanan bahan dapat bergantung pada konsentrasi, konteks penggunaan, dan sensitivitas individu. Selalu konsultasikan dengan dermatologis untuk masalah kulit yang serius.</p>
                </div>

                <h3>📞 Kontak & Dukungan</h3>
                <p>Jika Anda memiliki pertanyaan, saran, atau menemukan kesalahan dalam aplikasi ini, jangan ragu untuk menghubungi tim pengembang kami. Kami selalu terbuka untuk feedback dan perbaikan berkelanjutan.</p>
            </div>
        </section>
    </div>

    <script>
        // Database bahan berbahaya
        const dangerousIngredients = {
            'paraben': {
                'description': 'Dapat mengganggu sistem hormon (Regulasi EU No. 1223/2009)',
                'category': 'Pengganggu Endokrin',
                'risk_level': 'Tinggi',
                'common_names': ['methylparaben', 'propylparaben', 'butylparaben'],
                'details': 'Paraben adalah pengawet yang umum digunakan dalam kosmetik. Penelitian menunjukkan bahwa paraben dapat meniru estrogen dalam tubuh dan berpotensi mengganggu sistem endokrin. Beberapa negara telah membatasi penggunaan paraben tertentu dalam produk kosmetik.'
            },
            'sulfate': {
                'description': 'Bersifat keras dan dapat mengiritasi kulit sensitif',
                'category': 'Iritan',
                'risk_level': 'Sedang',
                'common_names': ['sodium lauryl sulfate', 'sls', 'sodium laureth sulfate'],
                'details': 'Sulfate adalah surfaktan yang digunakan untuk membuat busa dalam produk pembersih. Meskipun efektif membersihkan, sulfate dapat menghilangkan minyak alami kulit dan menyebabkan iritasi, terutama pada kulit sensitif atau kering.'
            },
            'phthalate': {
                'description': 'Dapat mengganggu hormon dan mempengaruhi kesehatan reproduksi (Regulasi EU No. 1223/2009)',
                'category': 'Pengganggu Endokrin',
                'risk_level': 'Tinggi',
                'common_names': ['dibutyl phthalate (dbp)', 'diethylhexyl phthalate (dehp)'],
                'details': 'Phthalate digunakan sebagai pelarut dan untuk meningkatkan fleksibilitas plastik. Penelitian menunjukkan bahwa phthalate dapat mengganggu sistem hormon dan dikaitkan dengan masalah reproduksi. Uni Eropa telah melarang beberapa jenis phthalate dalam kosmetik.'
            },
            'formaldehyde': {
                'description': 'Karsinogen yang diketahui dan dapat menyebabkan sensitisasi kulit',
                'category': 'Karsinogen, Alergen',
                'risk_level': 'Tinggi',
                'common_names': ['formalin', 'methylene glycol', 'quaternium-15'],
                'details': 'Formaldehyde adalah pengawet yang telah diklasifikasikan sebagai karsinogen oleh International Agency for Research on Cancer (IARC). Bahan ini dapat menyebabkan reaksi alergi dan iritasi kulit, serta berpotensi meningkatkan risiko kanker dengan paparan jangka panjang.'
            },
            'mercury': {
                'description': 'Neurotoksin, berbahaya bagi ginjal dan sistem saraf',
                'category': 'Logam Berat, Neurotoksin',
                'risk_level': 'Kritis',
                'common_names': ['calomel', 'mercuric chloride'],
                'details': 'Mercury adalah logam berat yang sangat beracun bagi sistem saraf, ginjal, dan organ lainnya. Meskipun dilarang dalam kosmetik di banyak negara, mercury masih ditemukan dalam beberapa produk pemutih kulit ilegal. Paparan mercury dapat menyebabkan kerusakan saraf permanen.'
            },
            'hydroquinone': {
                'description': 'Pemutih kulit, dapat menyebabkan ochronosis (perubahan warna kulit)',
                'category': 'Iritan Kulit, Pengganggu Pigmentasi',
                'risk_level': 'Tinggi',
                'common_names': ['dihydroxybenzene', 'quinol'],
                'details': 'Hydroquinone adalah agen pemutih kulit yang dapat menyebabkan ochronosis, suatu kondisi di mana kulit menjadi gelap dan menebal. Penggunaan jangka panjang juga dikaitkan dengan peningkatan risiko kanker kulit. Bahan ini dilarang dalam kosmetik di beberapa negara.'
            },
            'triclosan': {
                'description': 'Dapat mengganggu hormon dan berkontribusi pada resistensi antibiotik',
                'category': 'Pengganggu Endokrin, Resistensi Antibiotik',
                'risk_level': 'Tinggi',
                'common_names': ['triclosan', 'tcs'],
                'details': 'Triclosan adalah agen antimikroba yang dapat mengganggu fungsi hormon tiroid dan berkontribusi pada perkembangan bakteri yang resisten terhadap antibiotik. FDA telah melarang penggunaan triclosan dalam sabun antibakteri konsumen.'
            },
            'alcohol': {
                'description': 'Dapat membuat kulit kering dan iritasi pada beberapa jenis kulit (tergantung jenis dan konsentrasi)',
                'category': 'Iritan, Pengering',
                'risk_level': 'Sedang',
                'common_names': ['ethanol', 'isopropyl alcohol', 'sd alcohol'],
                'details': 'Alkohol dalam kosmetik dapat menghilangkan minyak alami kulit dan menyebabkan kekeringan serta iritasi. Namun, tidak semua alkohol berbahaya - fatty alcohol seperti cetyl alcohol justru dapat melembapkan kulit. Yang perlu diwaspadai adalah alkohol denaturing seperti ethanol.'
            },
            'fragrance': {
                'description': 'Alergen umum dan dapat menyebabkan iritasi kulit (sering merupakan campuran bahan kimia yang tidak diungkapkan)',
                'category': 'Alergen, Iritan',
                'risk_level': 'Sedang',
                'common_names': ['parfum', 'perfume', 'aroma'],
                'details': 'Fragrance atau parfum sering kali merupakan campuran dari puluhan bahkan ratusan bahan kimia yang tidak diungkapkan secara detail. Ini adalah salah satu penyebab utama reaksi alergi dan iritasi kulit dalam produk kosmetik. Orang dengan kulit sensitif disarankan untuk menghindari produk dengan fragrance.'
            },
            'lead': {
                'description': 'Neurotoksin, berbahaya bagi sistem saraf (terutama pada anak-anak)',
                'category': 'Logam Berat, Neurotoksin',
                'risk_level': 'Kritis',
                'common_names': ['lead acetate'],
                'details': 'Lead (timbal) adalah logam berat yang sangat beracun, terutama bagi sistem saraf. Paparan timbal dapat menyebabkan kerusakan otak, masalah pembelajaran pada anak-anak, dan berbagai masalah kesehatan lainnya. Timbal dilarang dalam kosmetik di banyak negara, namun masih dapat ditemukan sebagai kontaminan.'
            },
            'toluene': {
                'description': 'Dapat mempengaruhi sistem pernapasan dan sistem saraf',
                'category': 'Toksin',
                'risk_level': 'Tinggi',
                'common_names': ['methylbenzene', 'toluol'],
                'details': 'Toluene adalah pelarut yang dapat mempengaruhi sistem saraf pusat dan sistem pernapasan. Paparan jangka panjang dapat menyebabkan sakit kepala, pusing, dan masalah neurologis. Toluene sering ditemukan dalam cat kuku dan penghapus cat kuku.'
            },
            'bha': {
                'description': 'Kemungkinan pengganggu endokrin dan karsinogen',
                'category': 'Pengganggu Endokrin, Kemungkinan Karsinogen',
                'risk_level': 'Tinggi',
                'common_names': ['butylated hydroxyanisole'],
                'details': 'BHA (Butylated Hydroxyanisole) adalah antioksidan sintetis yang digunakan sebagai pengawet. Penelitian pada hewan menunjukkan bahwa BHA dapat menyebabkan tumor dan mengganggu sistem endokrin. International Agency for Research on Cancer mengklasifikasikan BHA sebagai kemungkinan karsinogen bagi manusia.'
            },
            'bht': {
                'description': 'Kemungkinan pengganggu endokrin dan alergen kulit',
                'category': 'Pengganggu Endokrin, Alergen',
                'risk_level': 'Sedang',
                'common_names': ['butylated hydroxytoluene'],
                'details': 'BHT (Butylated Hydroxytoluene) adalah antioksidan sintetis yang dapat menyebabkan reaksi alergi pada kulit dan berpotensi mengganggu sistem endokrin. Meskipun umumnya dianggap aman dalam konsentrasi rendah, beberapa negara telah membatasi penggunaannya dalam kosmetik.'
            },
            'petrolatum': {
                'description': 'Dapat terkontaminasi dengan PAH (polycyclic aromatic hydrocarbons) jika tidak dimurnikan dengan baik',
                'category': 'Risiko Kontaminan',
                'risk_level': 'Sedang',
                'common_names': ['petroleum jelly', 'mineral oil jelly'],
                'details': 'Petrolatum atau petroleum jelly sendiri umumnya aman, namun dapat terkontaminasi dengan PAH (polycyclic aromatic hydrocarbons) yang bersifat karsinogenik jika tidak dimurnikan dengan baik. Produk berkualitas tinggi biasanya telah dimurnikan untuk menghilangkan kontaminan ini.'
            },
            'phenoxyethanol': {
                'description': 'Pengawet, dapat menjadi alergen dan iritan kulit (dibatasi di beberapa negara)',
                'category': 'Pengawet, Alergen, Iritan',
                'risk_level': 'Sedang',
                'common_names': ['ethylene glycol phenyl ether'],
                'details': 'Phenoxyethanol adalah pengawet yang umum digunakan sebagai alternatif paraben. Meskipun umumnya dianggap lebih aman daripada paraben, phenoxyethanol masih dapat menyebabkan iritasi dan reaksi alergi pada beberapa orang, terutama dalam konsentrasi tinggi.'
            },
            'propylene glycol': {
                'description': 'Dapat menjadi iritan kulit dan alergen',
                'category': 'Iritan, Alergen',
                'risk_level': 'Sedang',
                'common_names': ['1,2-propanediol'],
                'details': 'Propylene glycol adalah humektan dan pelarut yang membantu produk menembus kulit. Namun, bahan ini dapat menyebabkan iritasi dan reaksi alergi, terutama pada orang dengan kulit sensitif atau dermatitis. Konsentrasi tinggi dapat meningkatkan risiko iritasi.'
            },
            'siloxane': {
                'description': 'Kemungkinan pengganggu endokrin (terutama siklosiloksan seperti cyclopent
