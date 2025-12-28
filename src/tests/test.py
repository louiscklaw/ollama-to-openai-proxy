#!/usr/bin/env python

# Add current directory to Python path for imports
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import test functions from existing modules
import test_openai
import test_generate
import test_chat


def main():
    """Main test runner - acts as a starter point for all endpoint tests"""

    print("=" * 80)
    print("OLLAMA-TO-OPENAI PROXY TEST SUITE")
    print("=" * 80)

    try:
        # Run all test functions
        print("\n🔍 Running all endpoint tests...")

        test_openai.test_tags_endpoint()
        print("\n" + "-" * 60)

        test_generate.test_generate_endpoint()
        print("\n" + "-" * 60)

        test_chat.test_chat_endpoint()

        print("\n" + "=" * 80)
        print("✅ All tests completed!")
        print("=" * 80)

        sys.exit(0)

    except KeyboardInterrupt:
        print("\n\n⚠️  Tests interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
