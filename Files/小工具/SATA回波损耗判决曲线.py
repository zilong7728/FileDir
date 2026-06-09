import math

def generate_sata_s1p(filename="SATA3_RX_Mask.s1p", device_type="RX"):
    """
    生成 SATA 3.0 Diff Return Loss Mask 的 S1P 文件
    device_type: "TX" 或 "RX"
    """
    f0 = 0.3  # 参考频率 GHz
    base_rl = 18 if device_type == "RX" else 14
    f_max = 6.0 if device_type == "RX" else 3.0
    
    with open(filename, 'w') as f:
        # --- 写入 Touchstone 标准头文件 ---
        f.write("! SATA 3.0 Differential Return Loss Mask\n")
        f.write(f"! Device Type: {device_type}\n")
        f.write("! Format: Frequency(GHz) Magnitude(dB) Phase(Degree)\n")
        
        # 核心设置行: 
        # GHz = 频率单位
        # S = S参数
        # DB = 幅度采用 dB，相位采用角度
        # R 100 = 参考阻抗设为 100 欧姆 (SATA 标准差分阻抗)
        f.write("# GHz S DB R 100\n")
        
        # --- 0 到 0.3 GHz 的低频平坦区 ---
        # 注意：标准 S 参数文件尽量避免绝对的 0 Hz (DC)，有些仿真器会报错。这里用 1kHz (1e-6 GHz) 替代。
        low_freqs_ghz = [1e-6, 0.001, 0.01, 0.1, 0.2, 0.3] 
        
        for freq in low_freqs_ghz:
            s_param_db = -base_rl
            phase = 0.0 # Limit Line 不需要实际相位，填入 0.0 占位
            f.write(f"{freq:.6f}\t{s_param_db:.4f}\t{phase:.1f}\n")
            
        # --- 0.3 GHz 以上的对数衰减区 (步长 100MHz) ---
        for freq_mhz in range(400, int(f_max * 1000) + 100, 100):
            freq_ghz = freq_mhz / 1000.0
            
            # 核心公式计算
            rl = base_rl - 13 * math.log10(freq_ghz / f0)
            s_param_db = -rl
            phase = 0.0
            
            f.write(f"{freq_ghz:.6f}\t{s_param_db:.4f}\t{phase:.1f}\n")
            
    print(f"成功生成 S1P 格式的 Mask 文件: {filename}")

# 运行函数生成 RX 的 Mask 文件
generate_sata_s1p(filename="SATA3_RX_Mask.s1p", device_type="RX")

# 如果需要 TX 的文件，解除下面这行的注释即可：
# generate_sata_s1p(filename="SATA3_TX_Mask.s1p", device_type="TX")
