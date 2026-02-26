from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'name': 'Himanshu Srivastava',
        'title': 'AI/ML Engineer & Full Stack Developer',
        'email': 'srivastavahimanshu071@gmail.com',
        'phone': '+91-9311415530',
        'linkedin': 'https://linkedin.com/in/himanshu071',
        'github': 'https://github.com/srivastava071',
        'education': {
            'university': 'Lovely Professional University',
            'location': 'Phagwara, Punjab',
            'degree': 'B.Tech in Computer Science (AI & ML)',
            'cgpa': '7.88',
            'period': 'Aug 2023 – Present'
        },
        'skills': {
            'Languages': ['JavaScript', 'C', 'C++', 'Python', 'Java', 'SQL', 'HTML/CSS'],
            'Tools & Platforms': ['Git', 'GitHub', 'Jupyter Notebook', 'Pandas', 'NumPy', 'Streamlit', 'Scikit-learn'],
            'Soft Skills': ['Analytical Problem-Solving', 'Cross-Functional Collaboration', 'Clear Communication', 'Adaptability']
        },
        'projects': [
            {
                'name': 'AI Agent for Business Decisions',
                'type': 'AI Project',
                'date': 'Dec 2025',
                'tech': ['Python', 'Pandas', 'NumPy', 'Google Colab', 'GitHub'],
                'points': [
                    'Built a Streamlit-based AI agent to support business decision-making using AI and rule-based logic.',
                    'Analyzed 100+ data records to generate insights and improve decision accuracy.'
                ],
                'icon': '🤖'
            },
            {
                'name': 'Real-Time Vehicle Tracking System',
                'type': 'ML Project',
                'date': 'Nov 2025',
                'tech': ['Python', 'Machine Learning', 'OpenCV', 'GPS', 'APIs'],
                'points': [
                    'Tracked 20+ vehicles in real time using ML-based detection and GPS data with 90%+ tracking accuracy.',
                    'Reduced manual monitoring by 40% through automated vehicle movement analysis and live updates.'
                ],
                'icon': '🚗'
            },
            {
                'name': 'Quiz Maze — Interactive Quiz Platform',
                'type': 'Web Project',
                'date': 'Jul 2025',
                'tech': ['HTML', 'CSS', 'JavaScript', 'Node.js', 'REST APIs'],
                'points': [
                    'Built an interactive quiz system with automated scoring and real-time leaderboard, supporting 100+ quiz attempts per session.',
                    'Implemented responsive UI and instant result updates, increasing user engagement across devices.'
                ],
                'icon': '🧩'
            },
            {
                'name': 'Automated Deadlock Detection Tool',
                'type': 'OS Project',
                'date': 'Apr 2025',
                'tech': ['Python', 'OS Concepts', 'Resource Allocation Graph', 'Web Dev'],
                'points': [
                    'Implemented a Python-based deadlock detection system analysing 50+ process-resource instances using Resource Allocation Graphs.',
                    'Built a web interface to visualize system states and detect deadlocks in real time, reducing analysis time by 35%.'
                ],
                'icon': '🔒'
            }
        ],
        'internship': {
            'company': 'Infosys Virtual Internship 6.0',
            'period': 'Feb 2026 | 8 weeks (Ongoing)',
            'points': [
                'Selected after successful completion of required courses and document verification.',
                'Working on a Voice Assistant–based Email Automation project using real-world problem statements.',
                'Developing and presenting the project following industry-standard practices.'
            ]
        },
        'certificates': [
            {'name': 'Winter Certification Program | CSRBOX X IBM - Applied AI', 'date': 'Dec 2025'},
            {'name': 'AI Primer Certification | Infosys Springboard', 'date': 'Dec 2025'},
            {'name': '24-Hour CTF Challenge (Concoction \'24) | upGrad', 'date': 'Apr 2024'},
            {'name': 'AI & ML Workshop | Tryst 2024 (IIT Delhi)', 'date': 'Mar 2024'},
            {'name': 'Open-Source Conference | OOSC 2024 (IIT Kanpur)', 'date': 'Aug 2024'},
        ],
        'activities': [
            'Member, Coding Ninjas — Event Management Volunteer for hackathons and DJ nights (Mar 2024–May 2025)',
            'LPU NSS Member — Contributed in social and environmental campaigns (Jun 2024–Jul 2024)',
            'Hostel Committee Member — Assisted in student management and welfare initiatives (Aug 2024–May 2025)'
        ]
    }
    return render_template('index.html', **data)

if __name__ == '__main__':
    app.run(debug=True)
