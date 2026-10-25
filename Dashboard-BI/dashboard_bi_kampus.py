import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Data ilustrasi untuk dashboard BI Kampus
prodi = ["TI", "SI", "MI", "AK", "DKV"]
ips_prodi = [3.4, 3.2, 3.0, 2.8, 3.1]
tunggakan = [6, 8, 12, 10, 7]

angkatan = ["2021", "2022", "2023", "2024"]
kehadiran = [87, 90, 86, 82]

fig = plt.figure(figsize=(15, 9), facecolor="#f3f6fb")
grid = fig.add_gridspec(3, 6, hspace=0.5, wspace=0.35)

fig.suptitle(
    "DASHBOARD BI KAMPUS",
    fontsize=23,
    fontweight="bold",
    color="#19345c",
    x=0.05, ha="left"
)

fig.text(
    0.05, 0.92,
    "Ringkasan performa akademik, kehadiran, dan keuangan",
    fontsize=11, color="#52627a"
)

# Enam kartu KPI
kpis = [
    ("1", "Rata-rata IPS mahasiswa", "3,12"),
    ("2", "Kehadiran mahasiswa < 75%", "12,5%"),
    ("3", "Rata-rata IPS per prodi", "3,08"),
    ("4", "Kehadiran per angkatan", "88,7%"),
    ("5", "Mahasiswa menunggak per prodi", "8,3%"),
    ("6", "Korelasi kehadiran dan IPS", "0,62")
]

colors = [
    "#dbeafe", "#fee2e2", "#d1fae5",
    "#fef3c7", "#e0e7ff", "#f3e8ff"
]

for i, (nomor, nama, nilai) in enumerate(kpis):
    ax = fig.add_subplot(grid[0, i])
    ax.set_facecolor(colors[i])
    ax.set_xticks([])
    ax.set_yticks([])

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.text(
        0.08, 0.85, nomor,
        fontsize=12, fontweight="bold",
        transform=ax.transAxes
    )
    ax.text(
        0.5, 0.55, nama,
        ha="center", va="center",
        fontsize=9, wrap=True,
        transform=ax.transAxes
    )
    ax.text(
        0.5, 0.20, nilai,
        ha="center", fontsize=19,
        fontweight="bold", color="#19345c",
        transform=ax.transAxes
    )

# KPI 3: IPS per program studi
ax = fig.add_subplot(grid[1, :2])
ax.bar(prodi, ips_prodi, color="#60a5fa")
ax.set_title("3. Rata-rata IPS per Prodi")
ax.set_ylabel("IPS")
ax.set_ylim(0, 4)
ax.grid(axis="y", alpha=0.2)
ax.set_axisbelow(True)

# KPI 4: Kehadiran per angkatan
ax = fig.add_subplot(grid[1, 2:4])
ax.bar(angkatan, kehadiran, color="#34d399")
ax.set_title("4. Kehadiran per Angkatan")
ax.set_ylabel("Kehadiran (%)")
ax.set_ylim(0, 100)
ax.grid(axis="y", alpha=0.2)
ax.set_axisbelow(True)

# KPI 2: Mahasiswa dengan kehadiran rendah
ax = fig.add_subplot(grid[1, 4:6])
ax.pie(
    [12.5, 87.5],
    labels=["Di bawah 75%", "75% ke atas"],
    autopct="%1.1f%%",
    colors=["#f87171", "#cbd5e1"],
    startangle=90
)
ax.set_title("2. Kelompok Kehadiran")

# KPI 5: Tunggakan per prodi
ax = fig.add_subplot(grid[2, :2])
ax.bar(prodi, tunggakan, color="#a78bfa")
ax.set_title("5. Mahasiswa Menunggak per Prodi")
ax.set_ylabel("Persentase (%)")
ax.set_ylim(0, 20)
ax.grid(axis="y", alpha=0.2)
ax.set_axisbelow(True)

# KPI 6: Korelasi kehadiran dan IPS
np.random.seed(10)
x = np.random.uniform(50, 100, 40)
y = 1 + 0.025 * (x - 50) + np.random.normal(0, 0.5, 40)
y = np.clip(y, 0, 4)

ax = fig.add_subplot(grid[2, 2:4])
ax.scatter(x, y, color="#818cf8", alpha=0.8)
garis = np.polyfit(x, y, 1)
ax.plot(
    [50, 100],
    np.polyval(garis, [50, 100]),
    color="#2563eb"
)
ax.set_title("6. Kehadiran dan IPS")
ax.set_xlabel("Kehadiran (%)")
ax.set_ylabel("IPS")
ax.set_ylim(0, 4)
ax.grid(alpha=0.2)

# KPI 1: Rata-rata IPS seluruh mahasiswa
ax = fig.add_subplot(grid[2, 4:6])
ax.set_title("1. Rata-rata IPS Mahasiswa")
ax.barh(["IPS"], [3.12], color="#3b82f6")
ax.set_xlim(0, 4)
ax.text(3.12, 0, " 3,12", va="center", fontweight="bold")
ax.axvline(3.5, color="red", linestyle="--", label="Target 3,50")
ax.legend(fontsize=8)
ax.grid(axis="x", alpha=0.2)
ax.set_axisbelow(True)

fig.text(
    0.05, 0.015,
    "Catatan: Seluruh angka merupakan data ilustrasi, bukan data resmi kampus.",
    fontsize=9, color="#52627a"
)

# plt.savefig(
#     "dashboard_bi_kampus.png",
#     dpi=160,
#     bbox_inches="tight"
# )

st.pyplot(fig)
