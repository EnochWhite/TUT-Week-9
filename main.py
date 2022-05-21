from travel import create_app

if __name__=='__main__':
    n_app=create_app()
    print('hi there')
    n_app.run(debug=True)