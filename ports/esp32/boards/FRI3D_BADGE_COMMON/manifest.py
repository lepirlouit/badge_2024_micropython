include("$(PORT_DIR)/boards/manifest.py")

package("fri3d", base_path="./modules")

module("boot.py", base_path="./modules")
module("main.py", base_path="./modules")
