<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arun Prakash S - AI Developer</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700&display=swap');
        
        :root {
            --primary-green: #00ff41;
            --secondary-green: #008f11;
            --dark-bg: #0d1117;
            --terminal-bg: #010409;
            --border-color: #30363d;
            --text-dim: #7d8590;
            --text-bright: #f0f6fc;
            --cursor-blink: 1.2s;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'JetBrains Mono', monospace;
            background: var(--dark-bg);
            color: var(--text-bright);
            line-height: 1.6;
            overflow-x: hidden;
        }

        /* Terminal Window */
        .terminal-window {
            background: var(--terminal-bg);
            border: 2px solid var(--border-color);
            border-radius: 12px;
            margin: 20px auto;
            max-width: 1200px;
            box-shadow: 0 20px 60px rgba(0, 255, 65, 0.1);
            overflow: hidden;
            animation: terminalGlow 3s ease-in-out infinite alternate;
        }

        @keyframes terminalGlow {
            0% { box-shadow: 0 20px 60px rgba(0, 255, 65, 0.1); }
            100% { box-shadow: 0 20px 80px rgba(0, 255, 65, 0.2); }
        }

        .terminal-header {
            background: var(--border-color);
            padding: 12px 20px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .terminal-buttons {
            display: flex;
            gap: 8px;
        }

        .btn {
            width: 12px;
            height: 12px;
            border-radius: 50%;
        }

        .btn.close { background: #ff5f56; }
        .btn.minimize { background: #ffbd2e; }
        .btn.maximize { background: #27ca3f; }

        .terminal-title {
            margin-left: auto;
            font-size: 12px;
            color: var(--text-dim);
            font-weight: 500;
        }

        .terminal-content {
            padding: 30px;
            min-height: 100vh;
        }

        /* Typing Animation */
        .prompt-line {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
        }

        .prompt {
            color: var(--primary-green);
            margin-right: 10px;
            font-weight: 600;
        }

        .typing {
            border-right: 2px solid var(--primary-green);
            animation: blink var(--cursor-blink) infinite;
        }

        @keyframes blink {
            0%, 50% { border-right-color: var(--primary-green); }
            51%, 100% { border-right-color: transparent; }
        }

        /* ASCII Art */
        .ascii-art {
            color: var(--primary-green);
            font-size: 10px;
            line-height: 1;
            margin: 20px 0;
            font-weight: 400;
        }

        /* Sections */
        .section {
            margin: 40px 0;
            opacity: 0;
            animation: fadeInUp 0.8s ease forwards;
        }

        .section:nth-child(2) { animation-delay: 0.5s; }
        .section:nth-child(3) { animation-delay: 1s; }
        .section:nth-child(4) { animation-delay: 1.5s; }
        .section:nth-child(5) { animation-delay: 2s; }

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

        .section-header {
            color: var(--primary-green);
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 15px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 5px;
        }

        /* Project Cards */
        .project-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .project-card {
            background: rgba(48, 54, 61, 0.3);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 20px;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .project-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 2px;
            background: linear-gradient(90deg, transparent, var(--primary-green), transparent);
            transition: left 0.5s ease;
        }

        .project-card:hover::before {
            left: 100%;
        }

        .project-card:hover {
            border-color: var(--primary-green);
            background: rgba(0, 255, 65, 0.05);
            transform: translateY(-5px);
        }

        .project-title {
            color: var(--primary-green);
            font-weight: 600;
            font-size: 16px;
            margin-bottom: 10px;
        }

        .project-desc {
            color: var(--text-dim);
            font-size: 14px;
            margin-bottom: 15px;
        }

        .project-tech {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }

        .tech-tag {
            background: rgba(0, 255, 65, 0.1);
            color: var(--primary-green);
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            border: 1px solid rgba(0, 255, 65, 0.3);
        }

        /* Stats Grid */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .stat-item {
            text-align: center;
            padding: 20px;
            background: rgba(48, 54, 61, 0.2);
            border-radius: 8px;
            border: 1px solid var(--border-color);
        }

        .stat-number {
            color: var(--primary-green);
            font-size: 32px;
            font-weight: 700;
            display: block;
        }

        .stat-label {
            color: var(--text-dim);
            font-size: 14px;
            margin-top: 5px;
        }

        /* Contact Links */
        .contact-links {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin-top: 20px;
        }

        .contact-link {
            color: var(--primary-green);
            text-decoration: none;
            padding: 10px 15px;
            border: 1px solid var(--primary-green);
            border-radius: 6px;
            transition: all 0.3s ease;
            font-size: 14px;
        }

        .contact-link:hover {
            background: var(--primary-green);
            color: var(--terminal-bg);
            box-shadow: 0 5px 15px rgba(0, 255, 65, 0.3);
        }

        /* Command History */
        .command-history {
            margin: 30px 0;
            padding: 20px;
            background: rgba(48, 54, 61, 0.2);
            border-radius: 8px;
            border-left: 4px solid var(--primary-green);
        }

        .command {
            display: flex;
            margin: 10px 0;
            font-size: 14px;
        }

        .command-prompt {
            color: var(--primary-green);
            margin-right: 10px;
        }

        .command-output {
            color: var(--text-dim);
        }

        /* Responsive */
        @media (max-width: 768px) {
            .terminal-window {
                margin: 10px;
                border-radius: 8px;
            }
            
            .terminal-content {
                padding: 20px;
            }
            
            .ascii-art {
                font-size: 8px;
            }
            
            .project-grid {
                grid-template-columns: 1fr;
            }
            
            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }

        ::-webkit-scrollbar-track {
            background: var(--terminal-bg);
        }

        ::-webkit-scrollbar-thumb {
            background: var(--primary-green);
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: var(--secondary-green);
        }
    </style>
</head>
<body>
    <div class="terminal-window">
        <div class="terminal-header">
            <div class="terminal-buttons">
                <div class="btn close"></div>
                <div class="btn minimize"></div>
                <div class="btn maximize"></div>
            </div>
            <div class="terminal-title">arun@homelab:~/portfolio — zsh — 80×24</div>
        </div>
        
        <div class="terminal-content">
            <div class="prompt-line">
                <span class="prompt">arun@homelab:~$</span>
                <span class="typing" id="typed-text"></span>
            </div>

            <div class="ascii-art">
    ╔═══════════════════════════════════════════════════════════════════════════╗
    ║   ▄▄▄       ██▀███   █    ██  ███▄    █     ██▓███   ██▀███   ▄▄▄        ║
    ║  ▒████▄    ▓██ ▒ ██▒ ██  ▓██▒ ██ ▀█   █    ▓██░  ██▒▓██ ▒ ██▒▒████▄      ║
    ║  ▒██  ▀█▄  ▓██ ░▄█ ▒▓██  ▒██░▓██  ▀█ ██▒   ▓██░ ██▓▒▓██ ░▄█ ▒▒██  ▀█▄    ║
    ║  ░██▄▄▄▄██ ▒██▀▀█▄  ▓▓█  ░██░▓██▒  ▐▌██▒   ▒██▄█▓▒ ▒▒██▀▀█▄  ░██▄▄▄▄██   ║
    ║   ▓█   ▓██▒░██▓ ▒██▒▒▒█████▓ ▒██░   ▓██░   ▒██▒ ░  ░░██▓ ▒██▒ ▓█   ▓██▒  ║
    ║   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒    ▒▓▒░ ░  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░  ║
    ║    ▒   ▒▒ ░  ░▒ ░ ▒░░░▒░ ░ ░ ░ ░░   ░ ▒░   ░▒ ░       ░▒ ░ ▒░  ▒   ▒▒ ░  ║
    ║    ░   ▒     ░░   ░  ░░░ ░ ░    ░   ░ ░    ░░         ░░   ░   ░   ▒     ║
    ║        ░  ░   ░        ░              ░                ░           ░  ░  ║
    ╚═══════════════════════════════════════════════════════════════════════════╝
                      Independent AI Developer & Researcher 
                           Coimbatore, Tamil Nadu, India
            </div>

            <div class="command-history">
                <div class="command">
                    <span class="command-prompt">$</span>
                    <span class="command-output">cat /etc/motd</span>
                </div>
                <div class="command">
                    <span class="command-prompt">></span>
                    <span class="command-output">Welcome to Arun's AI Development Environment</span>
                </div>
                <div class="command">
                    <span class="command-prompt">></span>
                    <span class="command-output">System Status: Online | Home Lab: Active | Projects: Running</span>
                </div>
            </div>

            <div class="section">
                <div class="section-header">ABOUT.md</div>
                <p style="color: var(--text-dim);">
                    Recent BCA (AI & DS) graduate passionate about building technology that solves real problems. 
                    Currently diving deep into Brain-Computer Interfaces, quantum-enhanced ML, and local AI systems.
                    I believe in privacy-first architecture, self-hosted solutions, and digital sovereignty.
                </p>
                
                <div class="stats-grid">
                    <div class="stat-item">
                        <span class="stat-number">15+</span>
                        <span class="stat-label">AI Projects</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-number">709</span>
                        <span class="stat-label">GitHub Followers</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-number">500+</span>
                        <span class="stat-label">LinkedIn Connections</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-number">24/7</span>
                        <span class="stat-label">Home Lab Uptime</span>
                    </div>
                </div>
            </div>

            <div class="section">
                <div class="section-header">FEATURED_PROJECTS.json</div>
                <div class="project-grid">
                    <div class="project-card">
                        <div class="project-title">🧠 Brain-Computer Interface Framework</div>
                        <div class="project-desc">Comprehensive modular BCI system with EEG analysis, motor imagery classification, and real-time processing pipelines. Features synthetic signal generation and PhysioNet dataset support.</div>
                        <div class="project-tech">
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">Signal Processing</span>
                            <span class="tech-tag">ML</span>
                            <span class="tech-tag">Real-time</span>
                        </div>
                    </div>

                    <div class="project-card">
                        <div class="project-title">🤖 Shendu: Local AI Assistant</div>
                        <div class="project-desc">Privacy-first AI assistant with custom Mistral-7B model, integrated with Obsidian vault. Features semantic search, background sync, and zero cloud dependencies.</div>
                        <div class="project-tech">
                            <span class="tech-tag">Local LLM</span>
                            <span class="tech-tag">Privacy-First</span>
                            <span class="tech-tag">Vector Search</span>
                            <span class="tech-tag">Obsidian API</span>
                        </div>
                    </div>

                    <div class="project-card">
                        <div class="project-title">⚛️ Quantum-Enhanced Neural Networks</div>
                        <div class="project-desc">Novel approach combining quantum computing with classical ML. Achieved 92% accuracy vs 85% classical, with 20% faster training using quantum-inspired feature mapping.</div>
                        <div class="project-tech">
                            <span class="tech-tag">Quantum Computing</span>
                            <span class="tech-tag">Qiskit</span>
                            <span class="tech-tag">Hybrid Systems</span>
                            <span class="tech-tag">Research</span>
                        </div>
                    </div>

                    <div class="project-card">
                        <div class="project-title">🌐 Distributed Healthcare Q&A System</div>
                        <div class="project-desc">Large-scale medical Q&A system using OPT-1.3B across multiple machines. Built with ZeroMQ, HuggingFace Transformers, and real-time dashboard.</div>
                        <div class="project-tech">
                            <span class="tech-tag">Distributed Systems</span>
                            <span class="tech-tag">LLM</span>
                            <span class="tech-tag">Healthcare</span>
                            <span class="tech-tag">ZeroMQ</span>
                        </div>
                    </div>

                    <div class="project-card">
                        <div class="project-title">👁️ Live Object Classification</div>
                        <div class="project-desc">Real-time webcam object detection with custom class training. Features confidence indicators, OpenCV integration, and intuitive user interface.</div>
                        <div class="project-tech">
                            <span class="tech-tag">Computer Vision</span>
                            <span class="tech-tag">OpenCV</span>
                            <span class="tech-tag">Real-time</span>
                            <span class="tech-tag">Classification</span>
                        </div>
                    </div>

                    <div class="project-card">
                        <div class="project-title">🏠 Home Lab Infrastructure</div>
                        <div class="project-desc">3-tier network with TrueNAS SCALE, PoE cameras, VLAN segmentation, and Tailscale remote access. Features ZFS snapshots and VM hosting.</div>
                        <div class="project-tech">
                            <span class="tech-tag">Networking</span>
                            <span class="tech-tag">TrueNAS</span>
                            <span class="tech-tag">Self-hosted</span>
                            <span class="tech-tag">ZFS</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="section">
                <div class="section-header">SKILLS.cfg</div>
                <div class="command-history">
                    <div class="command">
                        <span class="command-prompt">AI/ML:</span>
                        <span class="command-output">PyTorch, TensorFlow, HuggingFace, Transformers, LLMs, Computer Vision</span>
                    </div>
                    <div class="command">
                        <span class="command-prompt">Quantum:</span>
                        <span class="command-output">Qiskit, Quantum Circuits, Hybrid Classical-Quantum Systems</span>
                    </div>
                    <div class="command">
                        <span class="command-prompt">Languages:</span>
                        <span class="command-output">Python, JavaScript, R, HTML/CSS, Node.js</span>
                    </div>
                    <div class="command">
                        <span class="command-prompt">Infrastructure:</span>
                        <span class="command-output">TrueNAS, ZFS, Networking, Self-hosting, Tailscale</span>
                    </div>
                    <div class="command">
                        <span class="command-prompt">Specialties:</span>
                        <span class="command-output">Privacy-first AI, Local LLMs, Distributed Systems, BCI</span>
                    </div>
                </div>
            </div>

            <div class="section">
                <div class="section-header">CONTACT.sh</div>
                <div class="contact-links">
                    <a href="https://github.com/023b" class="contact-link">📁 GitHub</a>
                    <a href="https://linkedin.com/in/arun-prakash-s" class="contact-link">💼 LinkedIn</a>
                    <a href="mailto:arun@example.com" class="contact-link">📧 Email</a>
                    <a href="#" class="contact-link">🏠 Home Lab</a>
                </div>
            </div>

            <div class="prompt-line" style="margin-top: 40px;">
                <span class="prompt">arun@homelab:~$</span>
                <span class="typing">_</span>
            </div>
        </div>
    </div>

    <script>
        // Typing animation
        const texts = [
            "whoami",
            "cat README.md",
            "ls -la projects/",
            "./run_portfolio.sh",
            "echo 'Welcome to my digital space!'"
        ];
        
        let textIndex = 0;
        let charIndex = 0;
        const typedElement = document.getElementById('typed-text');
        
        function typeText() {
            if (charIndex < texts[textIndex].length) {
                typedElement.textContent += texts[textIndex].charAt(charIndex);
                charIndex++;
                setTimeout(typeText, 100);
            } else {
                setTimeout(eraseText, 2000);
            }
        }
        
        function eraseText() {
            if (charIndex > 0) {
                typedElement.textContent = texts[textIndex].substring(0, charIndex - 1);
                charIndex--;
                setTimeout(eraseText, 50);
            } else {
                textIndex = (textIndex + 1) % texts.length;
                setTimeout(typeText, 500);
            }
        }
        
        // Start typing animation
        setTimeout(typeText, 1000);

        // Add subtle glitch effect
        function addGlitch() {
            const cards = document.querySelectorAll('.project-card');
            cards.forEach(card => {
                card.addEventListener('mouseenter', () => {
                    card.style.textShadow = '0 0 10px rgba(0, 255, 65, 0.5)';
                });
                card.addEventListener('mouseleave', () => {
                    card.style.textShadow = 'none';
                });
            });
        }

        // Initialize effects
        window.addEventListener('load', addGlitch);

        // Matrix-style background effect
        function createMatrixRain() {
            const chars = "01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン";
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');
            
            canvas.style.position = 'fixed';
            canvas.style.top = '0';
            canvas.style.left = '0';
            canvas.style.width = '100%';
            canvas.style.height = '100%';
            canvas.style.zIndex = '-1';
            canvas.style.opacity = '0.03';
            
            document.body.appendChild(canvas);
            
            function resizeCanvas() {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            }
            
            resizeCanvas();
            window.addEventListener('resize', resizeCanvas);
            
            const drops = [];
            const columns = canvas.width / 20;
            
            for (let i = 0; i < columns; i++) {
                drops[i] = 1;
            }
            
            function drawMatrix() {
                ctx.fillStyle = 'rgba(1, 4, 9, 0.05)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                
                ctx.fillStyle = '#00ff41';
                ctx.font = '15px JetBrains Mono';
                
                for (let i = 0; i < drops.length; i++) {
                    const text = chars[Math.floor(Math.random() * chars.length)];
                    ctx.fillText(text, i * 20, drops[i] * 20);
                    
                    if (drops[i] * 20 > canvas.height && Math.random() > 0.975) {
                        drops[i] = 0;
                    }
                    
                    drops[i]++;
                }
            }
            
            setInterval(drawMatrix, 100);
        }
        
        // Uncomment to enable matrix effect
        // createMatrixRain();
    </script>
</body>
</html>
