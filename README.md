### Quick Start

1. Clone the repo
  ```
  $ git clone https://github.com/ttoti/blindbites2.0.git
  $ cd blindbites
  ```

2. Initialize and activate a virtualenv:
  ```
  $ virtualenv -p python2.x --no-site-packages env
  $ source env/bin/activate

  * For windows
  virtualenv --python=C:\Python2X\python.exe --no-site-packages env

  env\Scripts\activate
  ```

3. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```
4. Run the development server:
  ```
  $ python app.py
  ```

5. Navigate to [http://localhost:5000](http://localhost:5000)
