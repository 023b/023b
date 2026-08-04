# arun prakash s

AI/ML engineer working in edge computer vision, applied ML, and self-hosted infrastructure. Incoming MSc Computer Vision, Robotics & Machine Learning, University of Surrey, starting September 2026, Surrey Luminary Award scholar (GBP 7,000). BCA in AI & Data Science, Dr. M.G.R. Educational and Research Institute, Chennai, CGPA 8.02, 2022-2025.

Portfolio: 023b.pages.dev
LinkedIn: linkedin.com/in/arun-prakash-s-739881230
GitHub: github.com/023b

---

QbytX, AI Intern, May-Jun 2026, Chennai (remote)

Worked on the visual QC system for Mitsuba wiper motor production (W502 and YFG lines), formal title Computer Vision Intern, day to day closer to ML engineering. The system runs a 3-camera rig (top, front, back) with 6 TensorRT engines, detection and segmentation per camera, checking 16 quality control parameters and routing results through decision-fusion logic into CRITICAL, MEDIUM, and LOW severity tiers.

My work spanned the full pipeline:
- YOLOv8 detection and segmentation models for surface defects, missing components, and wrong markings on the conveyor line
- FastFlow anomaly detection (normalizing-flow based) for 5 soft/surface QC parameters that YOLOv8 alone couldn't catch, TensorRT FP16 optimized for real-time inference at 17-20ms per crop
- A connector classifier for YFG/YHB/YY8 connector types, a hybrid CNN (MobileNetV2 features) plus geometric descriptors, for multi-class identification in a live manufacturing setting
- Training scripts, threshold calibration, pipeline debugging, and packaging assets for team distribution

All deployed on Jetson Orin Nano under real hardware constraints, not benchmarked in isolation. Worked alongside Janarthanan (tech lead), Ashwin and Aravind (GPU compute, RTX 3060), and Sidhu (YOLO).

Rubixe, Data Science and AI Consultant, Nov 2025-Jul 2026, Bangalore

Eight months of applied data science and AI consulting work across client engagements.

DataMites, AI Engineering track, Aug 2025-Mar 2026

Completed all four AI Engineering capstones solo, end to end (EDA through evaluation), all graded A:
- Traffic Sign Detection (PRAICP-1002), 43-class GTSRB classification. Initial capped training set produced near-random accuracy; diagnosed as insufficient data for a 43-class fine-grained problem, retrained on the full ~39k images with early stopping. Best model (augmented, class-weighted CNN) beat MobileNetV2 transfer learning on macro-F1 (0.7932), MobileNetV2 underperformed due to domain mismatch between ImageNet pretraining and small iconographic sign crops
- Pneumonia Chest X-ray Classification (PRAICP-1012), binary medical imaging. MobileNetV2 transfer learning won clearly at 97%+ validation accuracy
- IndiSign Language Recognition (PRAICP-1000), 24-class ISL fingerspelling. Ran a quantitative leakage investigation on sequential capture data (MAE-ratio test) before training, used a contiguous purged split
- Dog Breeds-120 (PRAICP-1007), fine-grained classification. Correctly diagnosed underfitting rather than overfitting on from-scratch CNNs, applied the same leakage-check methodology, interpreted confusion pairs with domain knowledge (e.g. Eskimo dog vs. Siberian husky)

Also shipped the client project: a credit scoring model for Bank GoodCredit (PRCL-0015), LightGBM with Optuna tuning, Gini 32.85, benchmark to beat was 37.9. Key contribution was catching artifact features with inflated IV/WoE scores that were distorting model performance before they reached the final feature set. And a client-facing RAG chatbot (team PTID-AIE-APR-26-12003) on LangChain, OpenRouter, and ChromaDB.

Earlier: four Data Science track capstones (Bank GoodCredit, Rice Leaf Disease Detection with MobileNetV2/CNN, House Price Prediction with Gradient Boosting/Ridge, Home Loan Default Risk with LightGBM/Random Forest, Bike Rental Demand with XGBoost/Random Forest), all graded B, with specific feedback that shaped how I ran the AI Engineering track: be systematic about hyperparameter tuning instead of trial-and-error, justify every preprocessing decision, and make conclusions quantitative rather than vague.

IBM (via Prolearn), Cognitive Solutions and Technical Content Intern, Nov-Dec 2024, Chennai (hybrid)

Worked with IBM Watson and cognitive computing tools. Wrote technical documentation and blog content translating cognitive computing concepts for a non-specialist audience.

Pantech Solutions, AI Development Intern, Jan-Apr 2023, Chennai (remote)

First production ML exposure. Real-time AI implementation and ML integration in Python, training pipelines and model deployment workflows.

---

Homelab

Lancer, a Lenovo ThinkCentre M73 Tiny running Linux Mint, hosts my own infrastructure over Tailscale:

- LibreChat, self-hosted LLM chat with a custom OpenRouter cost-tracking layer I built on top
- Open WebUI, second local model interface
- Jellyfin, media server
- Immich, self-hosted photo/video backup
- Navidrome, self-hosted music streaming
- Filebrowser, web file management
- Home Assistant, home automation, wired into an ESP32-based IR remote system I built for a family member's bedroom
- Hermes (persona: Wes), a WhatsApp AI assistant built from scratch in Python, routes queries through OpenRouter (DeepSeek default) to local or cloud models, deployed as a Docker service
- Lancer Hub, a custom dashboard for the homelab itself, FastAPI backend on port 8899, tracks Docker services, system stats, and project status, built with a VHS/manga visual style

Secondary storage runs on a separate box being upgraded with new 1TB drives. Notes and journaling sync across devices via Logseq and Syncthing.

---

Other builds

- Signature verification using transfer learning, VGG16 adapted to a small dataset for genuine vs. forged classification (2023)
- Personalized GPT-2 chatbot, fine-tuned on biographical data with custom data pipelines and response-quality evaluation (2023)
- Real-time hand-tracking WebGL art, generative neon visuals driven by MediaPipe hand tracking
- BCI simulation framework, camera-based facial/body cue tracking used to simulate EEG-style signal processing and ML-based intent classification (ongoing)

---

Certifications

AI Engineer, DataMites, IABAC and NASSCOM certified, Aug 2025-Mar 2026
5-Day Gen AI Agents Intensive, Google/Kaggle
AI + Deep Learning, IIT Madras (Techobytes program)
Python for Data Science, IBM
Data Science with Python, TensorFlow/Keras, Data Mining, Great Learning (multiple courses)
Python Programming, Swayam/NPTEL

---

Stack

Machine learning and computer vision: PyTorch, OpenCV, YOLOv8, TensorRT, MobileNetV2/VGG16 transfer learning, FastFlow, scikit-learn, LightGBM, XGBoost, TensorFlow/Keras, Optuna
LLM and retrieval: LangChain, ChromaDB, Ollama, OpenRouter, Hugging Face
Infrastructure: Docker, Tailscale, Caddy, FastAPI, Linux (Mint/Ubuntu), systemd, MQTT
Languages and tools: Python, SQL, Bash, Git, Flask

---

Currently in Trichy, Tamil Nadu, relocating to Guildford, UK in September 2026 for the Surrey MSc.
