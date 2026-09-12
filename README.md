# 📱 SMS Spam Detection using SVM

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red.svg)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-Latest-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A machine learning-powered web application that classifies SMS messages as **SPAM** or **NOT SPAM** using Support Vector Machine (SVM) algorithm with TF-IDF vectorization.

## 🎯 Live Demo

Try the live application: [SMS Spam Detector](https://your-app-url.streamlit.app) *(Deploy and add your URL here)*

## 📊 About Support Vector Machine (SVM)

### What is SVM?

**Support Vector Machine (SVM)** is a powerful supervised machine learning algorithm used for both classification and regression tasks. In our case, we use it for **binary classification** to distinguish between spam and legitimate SMS messages.

### How SVM Works for Text Classification:

1. **Feature Extraction**: Text messages are converted into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency)
2. **Hyperplane Creation**: SVM finds the optimal hyperplane that separates spam and non-spam messages with maximum margin
3. **Support Vectors**: The algorithm identifies the most critical data points (support vectors) that define the decision boundary
4. **Classification**: New messages are classified based on which side of the hyperplane they fall

### Why SVM for Spam Detection?

- **High Accuracy**: Excellent performance on text classification tasks
- **Robust**: Works well with high-dimensional data (like text features)
- **Memory Efficient**: Only uses support vectors for predictions
- **Versatile**: Can handle both linear and non-linear classification with different kernels

## 🚀 Features

- ✅ **Real-time Classification**: Instantly classify SMS messages
- ✅ **User-friendly Interface**: Clean and intuitive Streamlit web app
- ✅ **High Accuracy**: Pre-trained SVM model with optimized performance
- ✅ **TF-IDF Vectorization**: Advanced text preprocessing and feature extraction
- ✅ **Responsive Design**: Works on desktop and mobile browsers
- ✅ **No Setup Required**: Ready-to-run application

## 🛠️ Technologies Used

| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Core programming language | 3.7+ |
| **Scikit-learn** | Machine learning algorithms | Latest |
| **Streamlit** | Web application framework | 1.0+ |
| **Pandas** | Data manipulation | Latest |
| **NumPy** | Numerical computations | Latest |
| **Joblib** | Model serialization | Latest |

## 📁 Project Structure

```
SMS_Spam_Detector/
│
├── app/
│   └── main.py                 # Streamlit web application
│
├── models/
│   ├── svm_model.pkl          # Trained SVM classifier
│   └── tfidf_vectorizer.pkl   # TF-IDF vectorizer
│
├── data/
│   └── spam_data.csv          # Training dataset
│
├── requirements.txt           # Python dependencies
├── README.md                 # Project documentation
└── .gitignore               # Git ignore rules
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mtechbro94/SMS-Spam-Detection-using-SVM.git
   cd SMS-Spam-Detection-using-SVM
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app/main.py
   ```

5. **Open your browser**
   The app will automatically open at `http://localhost:8501`

## 💻 Usage

1. **Enter SMS Text**: Type or paste an SMS message in the text area
2. **Click Predict**: Hit the "🔍 Predict" button
3. **View Results**: 
   - 🚨 **SPAM**: Message classified as spam
   - ✅ **NOT SPAM**: Message classified as legitimate

### Example Messages to Test:

**Spam Examples:**
- "URGENT! You've won $1000! Click here to claim your prize now!"
- "Free entry in 2 a weekly competition to win FA Cup final tickets. Txt WIN to 12345"

**Ham (Not Spam) Examples:**
- "Hey, are we still meeting for lunch tomorrow?"
- "Can you pick up some milk on your way home?"

## 🧠 Model Details

### Dataset
- **Source**: SMS Spam Collection Dataset
- **Size**: 5,574 SMS messages
- **Classes**: 
  - Ham (Not Spam): 4,827 messages (86.6%)
  - Spam: 747 messages (13.4%)

### Model Performance
- **Algorithm**: Support Vector Machine (SVM)
- **Kernel**: Linear
- **Feature Extraction**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Accuracy**: ~97% (approximate - update with your actual metrics)

### Preprocessing Pipeline
1. **Text Cleaning**: Remove special characters, convert to lowercase
2. **TF-IDF Vectorization**: Convert text to numerical features
3. **Feature Selection**: Optimize feature dimensions
4. **Model Training**: Train SVM classifier
5. **Model Serialization**: Save trained model and vectorizer

## 📊 Model Training Process

If you want to retrain the model:

1. **Prepare your dataset** in CSV format with columns: `text` and `label`
2. **Run the training script**:
   ```python
   from sklearn.model_selection import train_test_split
   from sklearn.feature_extraction.text import TfidfVectorizer
   from sklearn.svm import SVC
   from sklearn.metrics import accuracy_score
   import joblib
   import pandas as pd
   
   # Load and preprocess data
   df = pd.read_csv('spam_data.csv')
   X_train, X_test, y_train, y_test = train_test_split(
       df['text'], df['label'], test_size=0.2, random_state=42
   )
   
   # Vectorize text
   vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
   X_train_tfidf = vectorizer.fit_transform(X_train)
   X_test_tfidf = vectorizer.transform(X_test)
   
   # Train model
   model = SVC(kernel='linear', random_state=42)
   model.fit(X_train_tfidf, y_train)
   
   # Save model and vectorizer
   joblib.dump(model, 'svm_model.pkl')
   joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
   ```

## 🌐 Deployment

### Deploy to Streamlit Cloud

1. **Push to GitHub**: Ensure your code is on GitHub
2. **Visit Streamlit Cloud**: Go to [share.streamlit.io](https://share.streamlit.io)
3. **Connect Repository**: Link your GitHub repository
4. **Deploy**: Click deploy and share your app URL

### Deploy to Heroku

1. Create a `Procfile`:
   ```
   web: sh setup.sh && streamlit run app/main.py
   ```

2. Create `setup.sh`:
   ```bash
   mkdir -p ~/.streamlit/
   echo "\
   [general]\n\
   email = \"your-email@domain.com\"\n\
   " > ~/.streamlit/credentials.toml
   echo "\
   [server]\n\
   headless = true\n\
   enableCORS=false\n\
   port = $PORT\n\
   " > ~/.streamlit/config.toml
   ```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/AmazingFeature`
3. **Commit changes**: `git commit -m 'Add some AmazingFeature'`
4. **Push to branch**: `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

### Areas for Contribution:
- Improve model accuracy
- Add more preprocessing techniques
- Enhance UI/UX design
- Add batch processing feature
- Implement different ML algorithms
- Add performance metrics display

## 📈 Future Enhancements

- [ ] **Multi-language Support**: Detect spam in different languages
- [ ] **Batch Processing**: Upload and process multiple messages
- [ ] **API Integration**: RESTful API for programmatic access
- [ ] **Model Comparison**: Compare different ML algorithms
- [ ] **Real-time Learning**: Update model with user feedback
- [ ] **Advanced Analytics**: Detailed prediction confidence scores
- [ ] **Mobile App**: Native mobile application

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Mtechbro94**
- GitHub: [@mtechbro94](https://github.com/mtechbro94)
- Repository: [SMS-Spam-Detection-using-SVM](https://github.com/mtechbro94/SMS-Spam-Detection-using-SVM)

## 🙏 Acknowledgments

- **SMS Spam Collection Dataset** for providing the training data
- **Scikit-learn** community for excellent machine learning tools
- **Streamlit** team for the amazing web app framework
- **Open Source Community** for continuous inspiration and support

## 📞 Support

If you encounter any issues or have questions:

1. **Check the Issues**: Look at [existing issues](https://github.com/mtechbro94/SMS-Spam-Detection-using-SVM/issues)
2. **Create New Issue**: If your problem isn't listed, create a new issue
3. **Contact**: Reach out through GitHub

---

⭐ **If you found this project helpful, please give it a star!** ⭐

---

*Built with ❤️ using Python, Scikit-learn, and Streamlit*