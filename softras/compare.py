import matplotlib.pyplot as plt
import numpy as np
import sys
import os

def make_comparison_images(folder_name):
    target = plt.imread(f'{folder_name}/target.png')
    start = plt.imread(f'{folder_name}/start.png')
    final = plt.imread(f'{folder_name}/final.png')

    delta_start = target-start
    delta_final = target-final
    plt.clf()
    fig = plt.imshow(np.mean(np.abs(delta_start), axis=-1), cmap='plasma')
    plt.colorbar()
    plt.axis('off')
    plt.savefig(f'{folder_name}/delta_start.png', bbox_inches='tight')
    # plt.show()
    plt.clf()

    fig = plt.imshow(np.mean(np.abs(delta_final), axis=-1), cmap='plasma')
    plt.axis('off')
    plt.colorbar()
    plt.savefig(f'{folder_name}/delta_final.png', bbox_inches='tight')
    #plt.show()

    # Calculate RMS
    rms_start = np.sqrt(np.mean(delta_start**2))
    print(f"{folder_name} Initial RMS Error: {rms_start}")

    rms_final = np.sqrt(np.mean(delta_final ** 2))
    print(f"{folder_name} Final RMS Error: {rms_final}")


if __name__ == '__main__':
    try:
        folder_name = sys.argv[1]
    except:
        print("Specify folder name or 'all'")

    if folder_name == "all":
        root, dirs, files = next(os.walk('.'))
        for dir in dirs:
            try:
                make_comparison_images(dir)
            except(FileNotFoundError):
                print(f"Missing files in {dir}")
    else:
        make_comparison_images(folder_name)



