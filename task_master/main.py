from details.Console import Console


def main() -> None:
    """Main func"""
    # the tasks file get created at program start if not present
    
    presenter = Console()
    presenter.run()


if __name__ == "__main__":
    main()
