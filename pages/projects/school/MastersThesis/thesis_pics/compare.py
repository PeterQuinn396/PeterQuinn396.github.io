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

    delta_start = np.mean(np.abs(delta_start), axis=-1)
    delta_final = np.mean(np.abs(delta_final), axis=-1)

    vmin = 0
    vmax_start = np.max(delta_start)
    vmax_final = np.max(delta_final)
    vmax = max(vmax_start, vmax_final)


    fig = plt.imshow(delta_start, cmap='plasma', vmin=vmin, vmax = vmax)
    plt.axis('off')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)

    plt.savefig(f'{folder_name}/delta_start.png', bbox_inches='tight', pad_inches=0)

    cbar = plt.colorbar()
    fig.axes.remove()
    plt.savefig(f'{folder_name}/colour_bar.png', bbox_inches='tight', pad_inches=0)

    plt.clf()
    # plt.show()
    # plt.clf()

    fig = plt.imshow(delta_final, cmap='plasma', vmin=vmin, vmax = vmax)
    plt.axis('off')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    #plt.colorbar()
    plt.savefig(f'{folder_name}/delta_final.png', bbox_inches='tight', pad_inches=0)
    #plt.show()

    # Calculate RMS
    rms_start = np.sqrt(np.mean(delta_start**2))
    print(f"{folder_name} Initial RMS Error: {rms_start}")

    rms_final = np.sqrt(np.mean(delta_final ** 2))
    print(f"{folder_name} Final RMS Error: {rms_final}")

    with open(f'{folder_name}/metrics.txt', 'w+') as f:
        f.write(f'Initial RMS Error: {rms_start} \n')
        f.write(f'Final RMS Error: {rms_final}')



if __name__ == '__main__':
    try:
        folder_name = sys.argv[1]
    except:
        print("Specify folder name or 'all'")

    if folder_name == "-all":
        root, dirs, files = next(os.walk('.'))
        for dir in dirs:
            try:
                make_comparison_images(dir)
            except(FileNotFoundError):
                print(f"Missing files in {dir}")
    else:
        make_comparison_images(folder_name)



