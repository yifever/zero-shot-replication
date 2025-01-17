"""Base classes and enums for zero-shot replication problems."""
from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Generator, List, Tuple

OUTPUT_FILE_NAME = (
    "{PROVIDER}_{pset}__model_eq_{MODEL}__temperature_eq_{TEMPERATURE}.jsonl"
)


class ProblemType(Enum):
    """Type of problem to generate"""

    HUMAN_EVAL = "human-eval"
    LEETCODE = "leetcode"
    LEETCODE_MSFT_SPARKS = "leetcode-msft-sparks"
    GSM8K = "gsm8k"
    MATH = "math"


class BaseDataset(ABC):
    """An abstract class to provide problems for the runner."""

    @property
    @abstractmethod
    def raw_prompt(self) -> str:
        """Abstract method to get the raw prompt for this problems relating to this dataset."""
        pass

    @property
    @abstractmethod
    def input_paths(self) -> List[str]:
        """Abstract method to get a list over the input dataset paths"""
        pass

    @property
    @abstractmethod
    def generator(self) -> Generator[Tuple[str, Any], None, None]:
        """Abstract method to get a generator over the given problems"""
        pass

    @abstractmethod
    def get_formatted_prompt(
        self, problem: dict, completion: bool = False
    ) -> str:
        """Abstract method the formatted prompt for a problems relating to this dataset."""
        pass
