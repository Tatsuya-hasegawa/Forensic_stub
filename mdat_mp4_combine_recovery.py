import os,sys

def combine_files(set_pair,output_path):

    filename = set_pair[0].split("/")[-1].split("_")[0] + ".mov"
    with open(set_pair[0],"rb") as mdat:
        mdat_part = mdat.read()
    with open(set_pair[1],"rb") as mp4:
        mp4_part = mp4.read()
    combined_buf = mp4_part + mdat_part

    with open(output_path + "/" + filename,"wb") as combined:
        combined.write(combined_buf)
    print(f"Created. {filename}")

def process_files(directory,output_path):
    mdat_count = 0
    mp4_count = 0
    combine_count = 0

    for root, dirs, files in os.walk(directory):
        set_pair = []
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith("_mdat.mov") or file_path.endswith(".mp4"):
                print(file_path)
                if file_path.endswith("_mdat.mov"):
                    mdat_count += 1
                    set_pair.append(file_path)
                elif file_path.endswith(".mp4"):
                    mp4_count += 1
                    if len(set_pair)==0:
                        pass
                    elif len(set_pair)==1:
                        if set_pair[0].endswith("_mdat.mov"):
                            set_pair.append(file_path)
                            combine_files(set_pair,output_path)
                            combine_count += 1
                            set_pair = []
                            #sys.exit(1)
                    else:
                        print(f"Error! of {set_pair}")
                        set_pair = []

    print(f"{combine_count} files are probably recovered! (mdat:{mdat_count},mp4:{mp4_count})")

if __name__ == "__main__":
    directory_path = sys.argv[1]
    output_path = sys.argv[2]

    process_files(directory_path,output_path)