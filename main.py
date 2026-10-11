"""Giải phương trình ax² + bx + c = 0, kể cả nghiệm phức."""

import cmath
import math


def ve_nghiem(x_1, x_2):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)
    if x_1 == x_2:
        ax.scatter(x_1.real, x_1.imag, color="purple", s=80,
                   label=f"x₁ = x₂ = {x_1}")
        ax.annotate("x₁ = x₂", (x_1.real, x_1.imag),
                    xytext=(8, 8), textcoords="offset points")
    else:
        for root, label, color in ((x_1, "x₁", "blue"),
                                   (x_2, "x₂", "red")):
            ax.scatter(root.real, root.imag, color=color, s=80,
                       label=f"{label} = {root}")
            ax.annotate(label, (root.real, root.imag),
                        xytext=(8, 8), textcoords="offset points")
    margin = max(1, abs(x_1), abs(x_2)) * 0.25
    ax.set_xlim(min(0, x_1.real, x_2.real) - margin,
                max(0, x_1.real, x_2.real) + margin)
    ax.set_ylim(min(0, x_1.imag, x_2.imag) - margin,
                max(0, x_1.imag, x_2.imag) + margin)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("Phần thực Re(z)")
    ax.set_ylabel("Phần ảo Im(z)")
    ax.set_title("Hai nghiệm trên mặt phẳng phức")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18),
              fontsize=8)
    fig.tight_layout()
    fig.savefig("nghiem_phuc.png", dpi=150)
    print("Đã lưu đồ thị vào nghiem_phuc.png")
    plt.show()
    plt.close(fig)


def main():
    try:
        a = float(input("Nhập a: "))
        b = float(input("Nhập b: "))
        c = float(input("Nhập c: "))
        if not all(math.isfinite(value) for value in (a, b, c)):
            raise ValueError
    except ValueError:
        print("Vui lòng nhập các hệ số là số thực hữu hạn.")
        return

    delta = b * b - 4 * a * c
    print(f"Delta = {delta:g}")

    if a == 0:
        if b != 0:
            print(f"Phương trình bậc nhất có nghiệm x = {-c / b:g}")
        elif c == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
        return

    sqrt_delta = cmath.sqrt(delta)
    x_1 = (-b + sqrt_delta) / (2 * a)
    x_2 = (-b - sqrt_delta) / (2 * a)
    print(f"x_1 = {x_1}")
    print(f"x_2 = {x_2}")
    print("Trong Python, j là đơn vị ảo (j² = -1).")
    ve_nghiem(x_1, x_2)


if __name__ == "__main__":
    main()
