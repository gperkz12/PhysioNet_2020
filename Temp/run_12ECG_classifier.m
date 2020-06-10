function [score, label] = run_12ECG_classifier(data,header_data,classes, model)

    num_classes = length(classes);

    label = zeros([1,num_classes]);
    score = ones([1,num_classes]);
    
    % Use your classifier here to obtain a label and score for each class.
    features = get_12ECG_features(data,header_data);
    
    [label(1),s] = predict(model.AF.ClassificationSVM,features); score(1) = s(2);
    [label(2),s] = predict(model.IAVB.ClassificationSVM,features); score(2) = s(2);
    [label(3),s] = predict(model.LBBB.ClassificationKNN,features); score(3) = s(2);
    [label(4),s] = predict(model.Normal.ClassificationSVM,features); score(4) = s(2);
    [label(5),s] = predict(model.PAC.ClassificationKNN,features); score(5) = s(2);
    [label(6),s] = predict(model.PVC.ClassificationSVM,features); score(6) = s(2);
    [label(7),s] = predict(model.RBBB.ClassificationSVM,features); score(7) = s(2);
    [label(8),s] = predict(model.STD.ClassificationSVM,features); score(8) = s(2);
    [label(9),s] = predict(model.STE.ClassificationSVM,features); score(9) = s(2);
    
    % If more than one label is high, pick the highest score as the answer.
    % If the second-highest score is within half the value, select that one
    % as well.
    if sum(label) > 1
        tmpscore = score;
        label = zeros(1,9);
        [~,idx] = find(tmpscore==max(tmpscore));
        label(idx) = 1;
        m1 = tmpscore(idx);
        tmpscore(idx) = 0;
        [~,idx2] = find(tmpscore==max(tmpscore));
        m2 = tmpscore(idx2);
        if 2*m2 > m1
            label(idx2) = 1;
        end
    end
    
    % If no label is high, pick the highest nonzero score
    if sum(label) == 0
        [~,idx] = find(score == max(score(score~=0)));
        label(idx) = 1;
    end
end



