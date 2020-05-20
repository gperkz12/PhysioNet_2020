function extractAllFeatures(input_directory)

    
	% Find files.
    input_files = {};
    for f = dir(input_directory)'
        if exist(fullfile(input_directory, f.name), 'file') == 2 && f.name(1) ~= '.' && all(f.name(end - 2 : end) == 'mat')
            input_files{end + 1} = f.name;
        end
    end
    
    % read number of unique classes
    classes = get_classes(input_directory,input_files);
    num_classes = length(classes);

    % Iterate over files.
    disp('Extracting 12ECG Features...')
    num_files = length(input_files);
    num_features = 30;
    all_features = zeros(num_features,num_files);
    all_labels = zeros(num_classes,num_files);
    for i = 1:num_files
        disp(['    ', num2str(i), '/', num2str(num_files), '...'])

        % Load data.
        file_tmp=strsplit(input_files{i},'.');
        tmp_input_file = fullfile(input_directory, file_tmp{1});
        [data,header_data] = load_challenge_data(tmp_input_file);
        all_features(:,i) = get_12ECG_features(data,header_data);
                
        [~,~,tmp_labels]=get_true_labels([tmp_input_file '.hea'],classes);
        all_labels(:,i) = tmp_labels';
	
    end

    save('data_for_training','all_features','all_labels','classes');

    disp('Done.')
end


function [data,tlines] = load_challenge_data(filename)

        % Opening header file
        fid=fopen([filename '.hea']);
        if (fid<=0)
                disp(['error in opening file ' filename]);
        end

        tline = fgetl(fid);
        tlines = cell(0,1);
        while ischar(tline)
            tlines{end+1,1} = tline;
            tline = fgetl(fid);
        end
        fclose(fid);

        f=load([filename '.mat']);
        try
                data = f.val;
        catch ex
                rethrow(ex);
        end

end

% find unique number of classes
function classes = get_classes(input_directory,files)
	
	classes={};
	num_files = length(files);
	k=1;
    	for i = 1:num_files
		g = strrep(files{i},'.mat','.hea');
		input_file = fullfile(input_directory, g);
	        fid=fopen(input_file);
	        tline = fgetl(fid);
        	tlines = cell(0,1);

		while ischar(tline)
        	    tlines{end+1,1} = tline;
	            tline = fgetl(fid);
			if startsWith(tline,'#Dx')
				tmp = strsplit(tline,': ');
				tmp_c = strsplit(tmp{2},',');
				for j=1:length(tmp_c)
		                	idx2 = find(strcmp(classes,tmp_c{j}));
		                	if isempty(idx2)
                	        		classes{k}=tmp_c{j};
                        			k=k+1;
                			end
				end
			break
        		end
		end
        	fclose(fid);
	end
	classes=sort(classes)
end

function [recording_label,classes_label,single_recording_labels]=get_true_labels(input_file,classes)

	classes_label=classes;
	single_recording_labels=zeros(1,length(classes));

	fid=fopen(input_file);
        tline = fgetl(fid);
	tmp_str = strsplit(tline,' ');
	recording_label = tmp_str{1};

        tlines = cell(0,1);
        while ischar(tline)
	        tlines{end+1,1} = tline;
                tline = fgetl(fid);
        	if startsWith(tline,'#Dx')
                        tmp = strsplit(tline,': ');
                        tmp_c = strsplit(tmp{2},',');
                        for j=1:length(tmp_c)
                	        idx2 = find(strcmp(classes,tmp_c{j}));
				single_recording_labels(idx2)=1;
                        end
			break
                end
	end
        fclose(fid);

end