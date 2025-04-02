# filepath: c:\Users\admin\Desktop\touficAssessment\mini-library-management\backend\run.py
from app import create_app

app = create_app()

if __name__ == "__main__":
    # Run the app on 0.0.0.0 to make it accessible on the network
    app.run(host="0.0.0.0", port=5000, debug=True)