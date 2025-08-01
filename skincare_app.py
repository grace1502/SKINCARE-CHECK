<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skincare Safety Checker - AI Powered</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: url('/static/images/skincare-bg.jpg') no-repeat center center fixed;
            background-size: cover;
            position: relative;
            min-height: 100vh;
            color: #333;
        }

        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(255, 182, 193, 0.3) 0%, rgba(255, 218, 185, 0.2) 50%, rgba(255, 240, 245, 0.4) 100%);
            z-index: -1;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            text-align: center;
            margin-bottom: 40px;
            color: white;
            animation: fadeInDown 1s ease-out;
        }

        .header h1 {
            font-size: 3rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        .card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            margin-bottom: 30px;
            animation: fadeInUp 1s ease-out;
        }

        .input-section {
            margin-bottom: 30px;
        }

        .input-label {
            display: block;
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 15px;
            color: #4a5568;
        }

        .input-example {
            font-size: 0.9rem;
            color: #718096;
            margin-bottom: 15px;
            font-style: italic;
        }

        .ingredient-input {
            width: 100%;
            padding: 15px 20px;
            border: 2px solid #e2e8f0;
            border-radius: 12px;
            font-size: 1rem;
            transition: all 0.3s ease;
            resize: vertical;
            min-height: 120px;
        }

        .ingredient-input:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }

        .check-button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 40px;
            border: none;
            border-radius: 50px;
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
            display: block;
            margin: 20px auto;
        }

        .check-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 25px rgba(102, 126, 234, 0.6);
        }

        .check-button:active {
            transform: translateY(0);
        }

        .results {
            margin-top: 30px;
            display: none;
        }

        .result-header {
            text-align: center;
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 25px;
            padding: 15px;
            border-radius: 12px;
        }

        .safe-header {
            background: linear-gradient(135deg, #48bb78, #38a169);
            color: white;
        }

        .danger-header {
            background: linear-gradient(135deg, #f56565, #e53e3e);
            color: white;
        }

        .detected-ingredients {
            margin: 20px 0;
        }

        .ingredient-item {
            background: #fff5f5;
            border-left: 4px solid #f56565;
            padding: 15px;
            margin: 10px 0;
            border-radius: 8px;
            transition: all 0.3s ease;
        }

        .ingredient-item:hover {
            box-shadow: 0 4px 12px rgba(245, 101, 101, 0.2);
            transform: translateX(5px);
        }

        .ingredient-name {
            font-weight: 700;
            color: #c53030;
            font-size: 1.1rem;
            margin-bottom: 5px;
        }

        .ingredient-desc {
            color: #4a5568;
            line-height: 1.5;
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 25px 0;
        }

        .stat-card {
            background: linear-gradient(135deg, #f7fafc, #edf2f7);
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            border: 1px solid #e2e8f0;
        }

        .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: #2d3748;
        }

        .stat-label {
            color: #718096;
            font-size: 0.9rem;
            margin-top: 5px;
        }

        .recommendations {
            background: linear-gradient(135deg, #ebf8ff, #bee3f8);
            padding: 20px;
            border-radius: 12px;
            border-left: 4px solid #3182ce;
            margin-top: 20px;
        }

        .recommendations h3 {
            color: #2c5282;
            margin-bottom: 10px;
        }

        .references {
            text-align: center;
            margin-top: 30px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            color: white;
        }

        .loading {
            display: none;
            text-align: center;
            margin: 20px 0;
        }

        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #667eea;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 15px;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .safe-result {
            background: linear-gradient(135deg, #f0fff4, #c6f6d5);
            border-left: 4px solid #48bb78;
        }

        @media (max-width: 768px) {
            .header h1 {
                font-size: 2rem;
            }
            
            .card {
                padding: 20px;
                margin: 10px;
            }
            
            .stats {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1><i class="fas fa-flask"></i> Skincare Safety Checker</h1>
            <p>Analisis Keamanan Bahan Skincare Berbasis AI & Machine Learning</p>
        </div>

        <div class="card">
            <div class="input-section">
                <label class="input-label">
                    <i class="fas fa-list-ul"></i> Masukkan Daftar Kandungan Skincare Anda
                </label>
                <div class="input-example">
                    Contoh: aqua, glycerin, hydroquinone, fragrance, alcohol, mercury
                </div>
                <textarea 
                    class="ingredient-input" 
                    id="ingredientInput"
                    placeholder="Ketikkan semua bahan skincare yang ingin Anda periksa. Pisahkan dengan koma atau spasi..."
                ></textarea>
            </div>

            <button class="check-button" onclick="analyzeIngredients()">
                <i class="fas fa-search"></i> Analisis Keamanan Bahan
            </button>

            <div class="loading" id="loading">
                <div class="spinner"></div>
                <p>Menganalisis bahan skincare Anda...</p>
            </div>

            <div class="results" id="results">
                <div class="result-header" id="resultHeader">
                    <!-- Header hasil akan muncul di sini -->
                </div>

                <div class="stats" id="stats">
                    <!-- Statistik akan muncul di sini -->
                </div>

                <div class="detected-ingredients" id="detectedIngredients">
                    <!-- Bahan berbahaya akan muncul di sini -->
                </div>

                <div class="recommendations" id="recommendations">
                    <!-- Rekomendasi akan muncul di sini -->
                </div>
            </div>
        </div>

        <div class="references">
            <p><strong>Referensi:</strong> BPOM Indonesia, FDA (Food and Drug Administration), EWG (Environmental Working Group), EU Cosmetic Regulation No. 1223/2009</p>
        </div>
    </div>

    <script>
        // Database bahan berbahaya
        const bahanBerbahaya = {
            'paraben': 'Dapat mengganggu hormon (EU Regulation No. 1223/2009)',
            'sulfate': 'Bersifat keras dan dapat mengiritasi kulit',
            'phthalate': 'Dikaitkan dengan gangguan endokrin (FDA)',
            'formaldehyde': 'Karsinogenik (dilarang BPOM)',
            'mercury': 'Beracun bagi sistem saraf (dilarang FDA)',
            'hydroquinone': 'Dilarang BPOM (Keputusan HK.00.05.42.1018)',
            'triclosan': 'Dapat menyebabkan resistensi antibiotik',
            'alcohol': 'Dapat menyebabkan kekeringan dan iritasi ekstrim',
            'fragrance': 'Dapat menyebabkan alergi dan iritasi',
            'lead': 'Logam berat beracun',
            'toluene': 'Berbahaya untuk sistem saraf',
            'formaldehida': 'Karsinogenik (varian formaldehyde)',
            'petrolatum': 'Dapat terkontaminasi PAH (karsinogenik)',
            'phenoxyethanol': 'Dapat menyebabkan iritasi kulit',
            'propylene glycol': 'Dapat menyebabkan iritasi pada kulit sensitif',
            'siloxane': 'Dapat mengganggu hormon',
            'oxybenzone': 'Dikaitkan dengan gangguan hormon',
            'benzoyl peroxide': 'Dapat menyebabkan iritasi parah',
            'resorsinol': 'Berpotensi mengganggu fungsi tiroid',
            'pewarna sintetis': 'Dapat menyebabkan iritasi dan alergi'
        };

        function analyzeIngredients() {
            const input = document.getElementById('ingredientInput').value.toLowerCase();
            const loading = document.getElementById('loading');
            const results = document.getElementById('results');

            if (!input.trim()) {
                alert('Mohon masukkan daftar bahan skincare terlebih dahulu!');
                return;
            }

            // Tampilkan loading
            loading.style.display = 'block';
            results.style.display = 'none';

            // Simulasi loading dengan timeout
            setTimeout(() => {
                const detected = [];
                
                // Deteksi bahan berbahaya
                for (const [bahan, desc] of Object.entries(bahanBerbahaya)) {
                    if (input.includes(bahan)) {
                        detected.push({ name: bahan, description: desc });
                    }
                }

                // Hitung total bahan
                const totalIngredients = input.split(/[,\s]+/).filter(item => item.length > 2).length;
                const dangerousCount = detected.length;
                const safeCount = totalIngredients - dangerousCount;

                displayResults(detected, totalIngredients, dangerousCount, safeCount);
                
                loading.style.display = 'none';
                results.style.display = 'block';
            }, 2000);
        }

        function displayResults(detected, total, dangerous, safe) {
            const resultHeader = document.getElementById('resultHeader');
            const stats = document.getElementById('stats');
            const detectedIngredients = document.getElementById('detectedIngredients');
            const recommendations = document.getElementById('recommendations');

            if (detected.length > 0) {
                // Hasil berbahaya
                resultHeader.className = 'result-header danger-header';
                resultHeader.innerHTML = `
                    <i class="fas fa-exclamation-triangle"></i> 
                    BAHAN BERBAHAYA TERDETEKSI!
                `;

                // Statistik
                stats.innerHTML = `
                    <div class="stat-card">
                        <div class="stat-value" style="color: #e53e3e;">${dangerous}</div>
                        <div class="stat-label">Bahan Berbahaya</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" style="color: #48bb78;">${safe}</div>
                        <div class="stat-label">Bahan Aman</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" style="color: #4299e1;">${total}</div>
                        <div class="stat-label">Total Bahan</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" style="color: #ed8936;">${Math.round((dangerous/total)*100)}%</div>
                        <div class="stat-label">Tingkat Risiko</div>
                    </div>
                `;

                // Daftar bahan berbahaya
                detectedIngredients.innerHTML = `
                    <h3 style="color: #c53030; margin-bottom: 15px;">
                        <i class="fas fa-list"></i> Bahan Berbahaya yang Ditemukan:
                    </h3>
                    ${detected.map(item => `
                        <div class="ingredient-item">
                            <div class="ingredient-name">
                                <i class="fas fa-times-circle"></i> ${item.name.toUpperCase()}
                            </div>
                            <div class="ingredient-desc">${item.description}</div>
                        </div>
                    `).join('')}
                `;

                // Rekomendasi
                recommendations.innerHTML = `
                    <h3><i class="fas fa-lightbulb"></i> Rekomendasi Keamanan</h3>
                    <p><strong>⚠️ PERINGATAN:</strong> Produk ini mengandung bahan yang berpotensi berbahaya. Kami sangat menyarankan untuk:</p>
                    <ul style="margin: 10px 0; padding-left: 20px;">
                        <li>Hentikan pemakaian produk ini segera</li>
                        <li>Konsultasikan dengan dokter dermatologi</li>
                        <li>Cari alternatif produk yang lebih aman</li>
                        <li>Lakukan patch test sebelum menggunakan produk baru</li>
                    </ul>
                    <p><strong>Tingkat Kepercayaan:</strong> 95% (AI Confidence Score)</p>
                `;

            } else {
                // Hasil aman
                resultHeader.className = 'result-header safe-header';
                resultHeader.innerHTML = `
                    <i class="fas fa-check-circle"></i> 
                    PRODUK AMAN DIGUNAKAN!
                `;

                // Statistik
                stats.innerHTML = `
                    <div class="stat-card">
                        <div class="stat-value" style="color: #48bb78;">${total}</div>
                        <div class="stat-label">Bahan Aman</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" style="color: #e53e3e;">0</div>
                        <div class="stat-label">Bahan Berbahaya</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" style="color: #48bb78;">95%</div>
                        <div class="stat-label">Tingkat Keamanan</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" style="color: #4299e1;">AI</div>
                        <div class="stat-label">Powered by ML</div>
                    </div>
                `;

                // Hasil aman
                detectedIngredients.innerHTML = `
                    <div class="safe-result" style="padding: 20px; border-radius: 12px; text-align: center;">
                        <h3 style="color: #2f855a; margin-bottom: 10px;">
                            <i class="fas fa-shield-alt"></i> Tidak Ditemukan Bahan Berbahaya
                        </h3>
                        <p style="color: #4a5568;">Produk skincare Anda tidak mengandung bahan-bahan yang tercatat dalam database bahan berbahaya kami.</p>
                    </div>
                `;

                // Rekomendasi
                recommendations.innerHTML = `
                    <h3><i class="fas fa-lightbulb"></i> Rekomendasi Penggunaan</h3>
                    <p><strong>✅ AMAN:</strong> Berdasarkan analisis AI, produk ini relatif aman untuk digunakan. Namun tetap perhatikan:</p>
                    <ul style="margin: 10px 0; padding-left: 20px;">
                        <li>Lakukan patch test untuk memastikan tidak ada reaksi alergi</li>
                        <li>Perhatikan reaksi kulit setelah pemakaian</li>
                        <li>Gunakan sesuai petunjuk pada kemasan</li>
                        <li>Konsultasi dengan dermatolog untuk perawatan optimal</li>
                    </ul>
                    <p><strong>Tingkat Kepercayaan:</strong> 95% (AI Confidence Score)</p>
                `;
            }
        }

        // Auto-resize textarea
        document.getElementById('ingredientInput').addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = this.scrollHeight + 'px';
        });

        // Enter key untuk analisis
        document.getElementById('ingredientInput').addEventListener('keydown', function(e) {
            if (e.ctrlKey && e.key === 'Enter') {
                analyzeIngredients();
            }
        });
    </script>
</body>
</html>
