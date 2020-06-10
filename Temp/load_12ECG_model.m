function model = load_12ECG_model()

        filename='trained_model.mat';
        A=load(filename);
        model=A.model;

end


